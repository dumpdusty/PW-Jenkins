
from data.locators.base_locators import BaseLocator
    
class LoginPageLocator(BaseLocator):
    username_field = 'input#j_username'
    password_field = 'input[name="j_password"]'
    error_message = '.app-sign-in-register__error'
    checkbox = '.jenkins-checkbox'
        
