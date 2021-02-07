from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url[-6:-1] == 'login', "Wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_LINK), "Login register is not presented"
        
    def register_new_user(self, email, password = "12luker34567pr"):
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL_LINK)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD1_LINK)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.PASSWORD2_LINK)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_LINK )
        button.click()
        
             
        
    
        
        