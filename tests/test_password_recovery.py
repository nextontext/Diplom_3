import allure

from pages.forget_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from urls import BASE_URL
from helpers import generate_user


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_open_recover_password_page_from_login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(f"{BASE_URL}/login")
        login_page.open_recover_password_page()

        login_page.wait_url_contains("/forgot-password")

        assert "/forgot-password" in login_page.get_current_url()

    @allure.title("Переход к форме сброса пароля после ввода email")
    def test_recover_password_with_email(self, driver):
        user_data = generate_user()

        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_url(f"{BASE_URL}/forgot-password")
        forgot_password_page.recover_password(user_data["email"])
        
        forgot_password_page.wait_url_contains("/reset-password")

        assert "/reset-password" in forgot_password_page.get_current_url()

    @allure.title("Клик по кнопке показать пароль делает поле активным")
    def test_show_password_button_makes_password_field_active(self, driver):
        user_data = generate_user()
        
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_url(f"{BASE_URL}/forgot-password")
        forgot_password_page.recover_password(user_data["email"])

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.enter_new_password(user_data["password"])
        reset_password_page.click_show_password_button()

        assert reset_password_page.get_password_input_type() == "text"
