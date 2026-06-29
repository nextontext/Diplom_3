import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Ввести email на странице логина")
    def enter_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль на странице логина")
    def enter_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть по кнопке входа")
    def click_login_button(self):
        self.click_clickable_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизоваться пользователем")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Открыть страницу восстановления пароля")
    def open_recover_password_page(self):
        self.click_clickable_element(LoginPageLocators.RECOVER_PASSWORD_LINK)
