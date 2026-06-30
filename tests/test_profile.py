import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import BASE_URL


class TestProfile:

    @allure.title("Переход в личный кабинет")
    def test_open_personal_account(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.open_url(f"{BASE_URL}/login")
        login_page.login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        assert "/account/profile" in main_page.get_current_url()

    @allure.title("Переход в историю заказов")
    def test_open_order_history_from_profile(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.open_url(f"{BASE_URL}/login")
        login_page.login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        profile_page = ProfilePage(driver)
        profile_page.open_order_history()
        profile_page.wait_url_contains("/account/order-history")

        assert "/account/order-history" in profile_page.get_current_url()
    
    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.open_url(f"{BASE_URL}/login")
        login_page.login(
            create_user["email"],
            create_user["password"],
        )
        
        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        profile_page = ProfilePage(driver)
        profile_page.logout()
        profile_page.wait_url_contains("/login")

        assert "/login" in profile_page.get_current_url()
