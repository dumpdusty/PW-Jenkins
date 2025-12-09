import time
from playwright.sync_api import sync_playwright, expect

new_item_name = lambda issue_name: f"test{issue_name}_{int(time.time())}"
created_item_loc = lambda page, item_name: page.locator(f'td>a[href="job/{item_name}/"]')


def test_verify_create_freestyle_project(page):
    new_freestyle_project = new_item_name('freestyle_project')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_freestyle_project)
    page.get_by_text("Freestyle project", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect(created_item_loc(page, new_freestyle_project)).to_have_text(new_freestyle_project)    


def test_verify_create_pipeline(page):
    
    new_pipeline = new_item_name('pipeline')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_pipeline)
    page.get_by_text("Pipeline", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect((created_item_loc(page, new_pipeline))).to_have_text(new_pipeline)

def test_verify_create_mC_project(page):
    new_mf_project = new_item_name('mf_project')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_mf_project)
    page.get_by_text("Multi-configuration project", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect(created_item_loc(page, new_mf_project)).to_have_text(new_mf_project)    
    
    
def test_verify_create_folder(page):
    new_folder = new_item_name('folder')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_folder)
    page.get_by_text("Folder", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect(created_item_loc(page, new_folder)).to_have_text(new_folder)
    

def test_verify_create_mb_pipeline(page):
    new_mb_pipeline = new_item_name('mb_pipeline')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_mb_pipeline)
    page.get_by_text("Multibranch Pipeline", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect(created_item_loc(page, new_mb_pipeline)).to_have_text(new_mb_pipeline)    
   

def test_verify_create_org_folder(page):
    new_org_folder = new_item_name('org_folder')
    
    page.goto("/")
    
    page.locator('a:has-text("New Item")').click()
    page.locator('input#name').fill(new_org_folder)
    page.get_by_text("Organization Folder", exact=True).click()
    page.locator('button#ok-button').click()
    page.locator('.app-jenkins-logo').click()
    
    expect(created_item_loc(page, new_org_folder)).to_have_text(new_org_folder)