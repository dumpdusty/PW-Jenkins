import time
from playwright.sync_api import sync_playwright, expect


def test_verify_add_and_delete_description(page):
    
    random_text = f'test_description_{int(time.time())}'
    page.goto('/')
    page.locator('#description-link').click()
    page.locator('[name="description"]').fill(random_text)
    page.locator('[name="Submit"]').click()
    
    expect(page.locator('#description-content')).to_have_text(random_text)
    
    page.locator('#description-link').click()
    page.locator('[name="description"]').clear()
    page.locator('[name="Submit"]').click()
    
    expect(page.locator('#description-content')).to_be_empty()
    