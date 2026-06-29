import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import BASE_URL


class TestConstructor:

    @allure.title("Переход в конструктор из личного кабинета")
    @allure.title("Переход в конструктор из личного кабинета")
    def test_open_constructor_from_profile(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        main_page.open_constructor()

        assert main_page.is_constructor_opened()

    @allure.title("Переход в ленту заказов")
    def test_open_order_feed(self, driver):
        driver.get(BASE_URL)

        MainPage(driver).open_order_feed()

        MainPage(driver).wait_url_contains("/feed")

    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, driver):
        driver.get(BASE_URL)

        MainPage(driver).open_first_ingredient_details()

        assert MainPage(driver).is_ingredient_details_opened()
    
    @allure.title("Закрытие деталей ингредиента по клику на крестик")
    def test_close_ingredient_details_by_close_button(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.open_first_ingredient_details()
        main_page.close_ingredient_details()

        assert main_page.is_ingredient_details_closed()

    @allure.title("Счётчики ингредиентов увеличиваются после добавления в заказ")
    def test_ingredient_counters_increase_after_adding_to_order(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.drag_first_bun_to_constructor()

        assert main_page.get_first_bun_counter() == "2"

        main_page.open_sauces_tab()

        main_page.drag_first_sauce_to_constructor()

        assert main_page.get_first_sauce_counter() == "1"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        main_page.create_burger()
        main_page.click_order_button()

        assert main_page.is_order_modal_opened()
        assert main_page.get_order_number().isdigit()
