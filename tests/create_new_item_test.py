import time
from playwright.sync_api import sync_playwright, expect

new_item_name = lambda issue_name: f"test{issue_name}_{int(time.time())}"


def new_item_name(issue_name):
    return f"test_{issue_name}_{int(time.time())}"


def test_verify_create_new_pipeline(page):
    
    new_pipeline = new_item_name('pipeline')
    
    created_item_loc = page.locator(f'td>a[href="job/{new_pipeline}/"]')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_pipeline)
    page.get_by_text("Pipeline", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect((created_item_loc)).to_have_text(new_pipeline)
    
    
def test_verify_create_new_folder(page):
    new_folder = new_item_name('folder')
    created_item_loc = page.locator(f'td>a[href="job/{new_folder}/"]')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_folder)
    page.get_by_text("Folder", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect(created_item_loc).to_have_text(new_folder)
    
   