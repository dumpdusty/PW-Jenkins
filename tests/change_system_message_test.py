from playwright.sync_api import sync_playwright, expect

def test_verify_system_message_change(page):
    page.goto('/')
    page.locator('#root-action-ManageJenkinsAction').click()
    page.locator('a[href="configure"]').click()
    page.locator('textarea[name="system_message"]').fill('Welcome to Jenkins!')
    page.get_by_role('button', name='Save').click()
    
    expect(page.locator('#systemmessage')).to_have_text('Welcome to Jenkins!')
    
    page.locator('#root-action-ManageJenkinsAction').click()
    page.locator('a[href="configure"]').click()
    page.locator('textarea[name="system_message"]').clear()
    page.get_by_role('button', name='Save').click()
    
    expect(page.locator('#systemmessage')).to_be_empty()