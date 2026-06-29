from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    def enter_email(self, email):
        self.set_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click_clickable_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    def recover_password(self, email):
        self.enter_email(email)
        self.click_recover_button()
