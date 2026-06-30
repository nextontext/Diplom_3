import allure

from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step("Ввести новый пароль")
    def enter_new_password(self, password):
        self.set_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть по кнопке показать пароль")
    def click_show_password_button(self):
        self.click_clickable_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Получить тип поля ввода пароля")
    def get_password_input_type(self):
        return self.get_attribute(ResetPasswordPageLocators.PASSWORD_INPUT, "type")

    @allure.step("Получить класс контейнера поля ввода пароля")
    def get_password_field_class(self):
        return self.get_attribute(
            ResetPasswordPageLocators.PASSWORD_INPUT_CONTAINER,
            "class",
        )
