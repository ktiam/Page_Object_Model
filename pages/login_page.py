from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # ���������� �������� �� ���������� url �����
        assert self.browser.current_url[-6:-1] == 'login', "Wrong url"

    def should_be_login_form(self):
        # ���������� ��������, ��� ���� ����� ������
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        # ���������� ��������, ��� ���� ����� ����������� �� ��������
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_LINK), "Login register is not presented"
        
        