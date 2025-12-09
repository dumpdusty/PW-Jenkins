from playwright.sync_api import sync_playwright, expect
import os
from dotenv import load_dotenv

load_dotenv() 


def test_login_successful(page):
    page.goto('/login?from=%2F')
    expect(page).to_have_title('Sign in - Jenkins')
    expect(page.locator('h1')).to_have_text('Sign in to Jenkins')
    
    page.locator("#j_username").press_sequentially(os.getenv("LOGIN"))
    page.locator("#j_password").press_sequentially(os.getenv("PASSWORD"))
    page.locator('button[name="Submit"]').click()
    
    expect(page).to_have_title('Dashboard - Jenkins')
    expect(page.locator('h1')).to_have_text('Welcome to Jenkins!')
    
def test_login_invalid_username(page):
    page.goto('/login?from=%2F')
    page.locator("#j_username").fill("invalid")
    page.locator("#j_password").fill(os.getenv("PASSWORD"))
    page.locator('button[name="Submit"]').click()
    
    expect(page.locator('.app-sign-in-register__error')).to_be_visible()
    expect(page.locator('.app-sign-in-register__error')).to_have_text('Invalid username or password')
    
    
def test_login_invalid_password(page):
    page.goto('/login?from=%2F')
    page.locator("#j_username").fill(os.getenv("LOGIN"))
    page.locator("#j_password").fill("invalid")
    page.locator('button[name="Submit"]').click()
    
    expect(page.locator('.app-sign-in-register__error')).to_be_visible()
    expect(page.locator('.app-sign-in-register__error')).to_have_text('Invalid username or password')