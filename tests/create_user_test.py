import time
from playwright.sync_api import sync_playwright, expect

def test_verify_user_created(page):
    created_user_loc = lambda name: f'td>a[href="user/{name.lower()}/"]'
    new_user = f'new_user_{int(time.time())}'
    
    page.goto('/manage/securityRealm/')
    
    page.locator('[href="addUser"]').click()
    page.locator('[name="username"]').fill(new_user)
    page.locator('[name="password1"]').fill('Pirate666!')
    page.locator('[name="password2"]').fill('Pirate666!')
    page.locator('[name="fullname"]').fill('Jack Sparrow')
    page.locator('[name="email"]').fill('jacksparrow@pirate.com')
    page.locator('[name="Submit"]').click()
    
    
    expect(page.locator(created_user_loc(new_user))).to_have_text(new_user)
    
    
    ## delete created user
    
    created_users_list = page.locator('a[data-title="Users"]')
    
    count = created_users_list.count()
    
    for _i in range(count):
        users = created_users_list
        if count > 0:
            users.first.click()
            page.locator('[data-id="ok"]').click()
        else:
            break    
    
    
    