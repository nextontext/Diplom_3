import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести email на странице восстановлдения пароля")
    def enter_email(self, email):
        self.set_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Кликнуть по кнопке восстановления пароля")
    def click_recover_button(self):
        self.click_clickable_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step("Восстановить пароль по email")
    def recover_password(self, email):
        self.enter_email(email)
        self.click_recover_button()
