import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from urls import BASE_URL


class TestOrderFeed:

    @allure.title("Открытие деталей заказа из ленты заказов")
    def test_open_order_details_from_order_feed(self, driver):
        driver.get(BASE_URL)

        MainPage(driver).open_order_feed()
        MainPage(driver).wait_url_contains("/feed")

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_first_order()

        assert order_feed_page.is_order_modal_opened()
        assert order_feed_page.is_order_composition_visible()
        assert "#" in order_feed_page.get_order_number_from_modal()

    @allure.title("Заказ пользователя отображается в ленте заказов")
    def test_user_order_from_history_is_visible_in_order_feed(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        main_page.create_burger()
        main_page.click_order_button()

        main_page.close_order_modal()
        main_page.open_personal_account()
        main_page.wait_url_contains("/account/profile")

        profile_page = ProfilePage(driver)
        profile_page.open_order_history()
        profile_page.wait_url_contains("/account/order-history")

        order_number = profile_page.get_first_order_number_from_history()

        main_page.open_order_feed()
        main_page.wait_url_contains("/feed")

        assert OrderFeedPage(driver).is_order_number_visible_in_feed(order_number)

    @allure.title("Счётчик выполненных заказов за всё время увеличивается после создания заказа")
    def test_total_done_counter_increases_after_order_created(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_order_feed()
        main_page.wait_url_contains("/feed")

        order_feed_page = OrderFeedPage(driver)
        total_done_before = order_feed_page.get_total_done_counter()

        main_page.open_constructor()
        main_page.create_burger()
        main_page.click_order_button()

        main_page.close_order_modal()
        main_page.open_order_feed()
        main_page.wait_url_contains("/feed")

        total_done_after = order_feed_page.get_total_done_counter()

        assert int(total_done_after) > int(total_done_before)

    @allure.title("Счётчик выполненных заказов за сегодня увеличивается после создания заказа")
    def test_today_done_counter_increases_after_order_created(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )
        main_page = MainPage(driver)
        assert main_page.is_constructor_opened()

        main_page.open_order_feed()
        main_page.wait_url_contains("/feed")

        order_feed_page = OrderFeedPage(driver)
        today_done_before = order_feed_page.get_today_done_counter()

        main_page.open_constructor()
        main_page.create_burger()
        main_page.click_order_button()

        main_page.close_order_modal()
        main_page.open_order_feed()
        main_page.wait_url_contains("/feed")

        today_done_after = order_feed_page.get_today_done_counter()

        assert int(today_done_after) > int(today_done_before)

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_number_appears_in_progress_after_order_created(self, driver, create_user):
        driver.get(f"{BASE_URL}/login")

        LoginPage(driver).login(
            create_user["email"],
            create_user["password"],
        )

        main_page = MainPage(driver)
        main_page.create_burger()
        main_page.click_order_button()

        assert main_page.is_order_modal_opened()

        main_page.wait_order_number_loaded()
        order_number = main_page.get_order_number()

        main_page.close_order_modal()
        main_page.open_order_feed()
        main_page.wait_url_contains("/feed")

        order_feed_page = OrderFeedPage(driver)

        print("ORDER NUMBER:", order_number)
        print("IN PROGRESS:", order_feed_page.get_in_progress_orders_text())

        assert order_number in order_feed_page.get_in_progress_orders_text()
