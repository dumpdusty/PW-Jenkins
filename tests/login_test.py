from data.locators.login_page_locators import LoginPageLocator
from data.endpoints import Endpoints
from data.error_message import ErrorMessage
from pages.login_page import LoginPage
from data.assertions import Assertions
from data.info.login_page_info import LoginPageInfo
from data.info.main_page_info import MainPageInfo

class TestLoginPage:
    locator = LoginPageLocator()
    endpoint = Endpoints()
    error = ErrorMessage()
    assertion = Assertions()
    login_info = LoginPageInfo()
    main_info = MainPageInfo()


    def test_login_successful(self, page):
        login_page = LoginPage(page, self.endpoint.login)

        login_page.open()

        self.assertion.verify_element_visible(page, self.locator.checkbox)
        self.assertion.verify_text(page, self.locator.checkbox, self.login_info.checkbox_info)

        self.assertion.verify_page_title(page, self.login_info.page_title)
        self.assertion.verify_text(page, self.locator.header, self.login_info.header)
        
        login_page.submit_login()
        
        self.assertion.verify_page_title(page, self.main_info.page_title)
        self.assertion.verify_text(page, self.locator.header, self.main_info.header)
        
    def test_login_invalid_username(self, page):
        login_page = LoginPage(page, self.endpoint.login)

        login_page.open()
        
        login_page.submit_login(username = 'invalid')
        
        self.assertion.verify_element_visible(page, self.locator.error_message)
        self.assertion.verify_text(page, self.locator.error_message, self.error.invalid_login_credentials)
        
        
    def test_login_invalid_password(self, page):
        login_page = LoginPage(page, self.endpoint.login)

        login_page.open()
        
        login_page.submit_login(password = 'invalid')
        
        self.assertion.verify_element_visible(page, self.locator.error_message)
        self.assertion.verify_text(page, self.locator.error_message, self.error.invalid_login_credentials)