from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_clickable_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def open_recover_password_page(self):
        self.click_clickable_element(LoginPageLocators.RECOVER_PASSWORD_LINK)
