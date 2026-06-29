from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    def enter_new_password(self, password):
        self.set_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    def click_show_password_button(self):
        self.click_clickable_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def get_password_input_type(self):
        return self.get_attribute(ResetPasswordPageLocators.PASSWORD_INPUT, "type")

    def get_password_field_class(self):
        return self.get_attribute(
            ResetPasswordPageLocators.PASSWORD_INPUT_CONTAINER,
            "class",
        )
