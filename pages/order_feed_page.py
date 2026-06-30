import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Открыть первый заказ в ленте заказов")
    def open_first_order(self):
        self.click_clickable_element(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step("Проверить, что модальное окно заказа открыто")
    def is_order_modal_opened(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_MODAL)

    @allure.step("Проверить, что состав заказа отображается")
    def is_order_composition_visible(self):
        return self.is_element_visible(
            OrderFeedPageLocators.ORDER_MODAL_COMPOSITION_TITLE
        )

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text(OrderFeedPageLocators.ORDER_MODAL_NUMBER)

    @allure.step("Проверить, что заказ отображается в ленте заказов")
    def is_order_number_visible_in_feed(self, order_number):
        return self.is_element_visible(
            OrderFeedPageLocators.order_number_in_feed(order_number)
        )

    @allure.step("Получить счётчик выполненных заказов за всё время")
    def get_total_done_counter(self):
        return self.get_text(OrderFeedPageLocators.TOTAL_DONE_COUNTER)
    
    @allure.step("Получить счётчик выполненных заказов за сегодня")
    def get_today_done_counter(self):
        return self.get_text(OrderFeedPageLocators.TODAY_DONE_COUNTER)
    
    @allure.step("Проверить, что заказ отображается в разделе 'В работе'")
    def is_order_number_in_progress_visible(self, order_number):
        return self.is_element_visible(
            OrderFeedPageLocators.order_number_in_progress(order_number)
        )

    @allure.step("Дождаться появления заказа в разделе В работе")
    def wait_order_number_in_progress_visible(self, order_number):
        self.wait_element_visible(
            OrderFeedPageLocators.order_number_in_progress(order_number),
            timeout=15,
        )
    
    @allure.step("Получить текст раздела 'В работе'")
    def get_in_progress_orders_text(self):
        return self.get_text(OrderFeedPageLocators.IN_PROGRESS_ORDERS_LIST)
