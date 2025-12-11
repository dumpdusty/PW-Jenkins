from data.locators.login_page_locators import LoginPageLocators
from data.endpoints import Endpoints
from data.error_message import ErrorMessage
from pages.login_page import LoginPage
from data.assertions import Assertions

class TestLoginPage:
    locator = LoginPageLocators()
    endpoint = Endpoints()
    error = ErrorMessage()
    assertion = Assertions()
    


    def test_login_successful(self, page):
        login_page = LoginPage(page, self.endpoint.login)

        login_page.open()
        
        self.assertion.verify_page_title(page, 'Sign in - Jenkins')
        self.assertion.verify_text(page, self.locator.header, 'Sign in to Jenkins')
        
        login_page.submit_login(self.locator)
        
        self.assertion.verify_page_title(page, 'Dashboard - Jenkins')
        self.assertion.verify_text(page, self.locator.header, 'Welcome to Jenkins!')
        
    def test_login_invalid_username(self, page):
        login_page = LoginPage(page, self.endpoint.login)

        login_page.open()
        
        login_page.submit_login(self.locator, username = 'invalid')
        
        self.assertion.verify_element_visible(page, self.locator.error_message)
        self.assertion.verify_text(page, self.locator.error_message, self.error.invalid_login_credentials)
        
        
    def test_login_invalid_password(self, page):
        login_page = LoginPage(page, self.endpoint.login)

        login_page.open()
        
        login_page.submit_login(self.locator, password = 'invalid')
        
        self.assertion.verify_element_visible(page, self.locator.error_message)
        self.assertion.verify_text(page, self.locator.error_message, self.error.invalid_login_credentials)