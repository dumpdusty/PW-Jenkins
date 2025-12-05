from playwright.sync_api import Playwright, ViewportSize
import pytest
import requests


api_token = '11e6d810528517fc78a862576cbe90539c'
user_name = 'dumpdusty'
url = 'http://localhost:8080'

@pytest.fixture(scope="function")
def get_cookies(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(
        base_url="http://localhost:8080/login?from=%2F"
    )
    page = context.new_page()
     
    page.goto("/")
    page.locator("#j_username").fill("dumpdusty")
    page.locator("#j_password").fill("W3ss3rv1@@")
    page.locator('button[name="Submit"]').click()
    cookies = context.cookies()
    
    page.close()
    context.close()
    browser.close()

    return cookies


@pytest.fixture
def page(playwright: Playwright, get_cookies):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport=ViewportSize(width=1280, height=920),
        base_url="http://localhost:8080/"
    )
    
    context.add_cookies(get_cookies)
    
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
    
    
    
def get_all_jobs():
    response = requests.get(
        url=f'{url}/api/json',
        auth=(user_name, api_token)
    )
    
    return response.json()['jobs']

def delete_jobs():
    jobs_list = get_all_jobs()
    for job in jobs_list:
        name = job['name']
        requests.post(
            url=f'{url}/job/{name}/doDelete',
            auth=(user_name, api_token)
        )


    
# @pytest.fixture(scope="session", autouse=True)
# def delete_all_jobs_after_test():
#     yield
#     delete_jobs()