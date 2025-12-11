from playwright.sync_api import sync_playwright, expect
import os
from dotenv import load_dotenv

from data.locators.login_page_locators import LoginPageLocators
from data.endpoints import Endpoints

load_dotenv()
locator = LoginPageLocators()
endpoint = Endpoints()


def test_login_successful(page):
    page.goto(endpoint.login)
    expect(page).to_have_title('Sign in - Jenkins')
    expect(page.locator(locator.header)).to_have_text('Sign in to Jenkins')
    
    page.locator(locator.username_field).press_sequentially(os.getenv("LOGIN"))
    page.locator(locator.password_field).press_sequentially(os.getenv("PASSWORD"))
    page.locator(locator.submit_btn).click()
    
    expect(page).to_have_title('Dashboard - Jenkins')
    expect(page.locator(locator.header)).to_have_text('Welcome to Jenkins!')
    
def test_login_invalid_username(page):
    page.goto(endpoint.login)
    page.locator(locator.username_field).fill("invalid")
    page.locator(locator.password_field).fill(os.getenv("PASSWORD"))
    page.locator(locator.submit_btn).click()
    
    expect(page.locator(locator.error_message)).to_be_visible()
    expect(page.locator(locator.error_message)).to_have_text('Invalid username or password')
    
    
def test_login_invalid_password(page):
    page.goto(endpoint.login)
    page.locator(locator.username_field).fill(os.getenv("LOGIN"))
    page.locator(locator.password_field).fill("invalid")
    page.locator(locator.submit_btn).click()
    
    expect(page.locator(locator.error_message)).to_be_visible()
    expect(page.locator(locator.error_message)).to_have_text('Invalid username or password')