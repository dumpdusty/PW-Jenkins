from playwright.sync_api import Playwright, ViewportSize
import pytest
import requests
import os
from dotenv import load_dotenv
from data.endpoints import Endpoints

load_dotenv() 


api_token = os.getenv('API_TOKEN')
username = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
url = os.getenv('BASE_URL')

@pytest.fixture(scope="function")
def get_cookies(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(
        base_url=url + "/login?from=%2F"
    )
    page = context.new_page()
     
    page.goto("/")
    page.locator("#j_username").fill(username)
    page.locator("#j_password").fill(password)
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
        base_url=url
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
        auth=(username, api_token)
    )
    
    return response.json()['jobs']

def delete_jobs():
    jobs_list = get_all_jobs()
    for job in jobs_list:
        name = job['name']
        requests.post(
            url=f'{url}/job/{name}/doDelete',
            auth=(username, api_token)
        )


    
@pytest.fixture(scope="session", autouse=True)
def delete_all_jobs_after_test():
    yield
    delete_jobs()