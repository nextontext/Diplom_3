import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import BASE_URL


class TestProfile:

    @allure.title("Переход в личный кабинет")
    def test_open_personal_account(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

    @allure.title("Переход в историю заказов")
    def test_open_order_history_from_profile(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        ProfilePage(driver).open_order_history()

        ProfilePage(driver).wait_url_contains("/account/order-history")
    
    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )
        
        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        ProfilePage(driver).logout()

        ProfilePage(driver).wait_url_contains("/login")
