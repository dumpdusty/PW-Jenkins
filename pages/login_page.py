from pages.base_page import BasePage
import os
from dotenv import load_dotenv
from data.locators.login_page_locators import LoginPageLocator
 
load_dotenv()

class LoginPage(BasePage):
    locator = LoginPageLocator()
    
    def submit_login(self, username = os.getenv("LOGIN"), password = os.getenv("PASSWORD")):
        self.input_data(self.locator.username_field, username)
        self.input_data(self.locator.password_field, password)
        self.click_on_elem(self.locator.submit_btn)