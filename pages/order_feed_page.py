from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderFeedPage(BasePage):

    def open_first_order(self):
        self.click_clickable_element(OrderFeedPageLocators.FIRST_ORDER)

    def is_order_modal_opened(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_MODAL)

    def is_order_composition_visible(self):
        return self.is_element_visible(
            OrderFeedPageLocators.ORDER_MODAL_COMPOSITION_TITLE
        )

    def get_order_number_from_modal(self):
        return self.get_text(OrderFeedPageLocators.ORDER_MODAL_NUMBER)

    def is_order_number_visible_in_feed(self, order_number):
        return self.is_element_visible(
            OrderFeedPageLocators.order_number_in_feed(order_number)
        )

    def get_total_done_counter(self):
        return self.get_text(OrderFeedPageLocators.TOTAL_DONE_COUNTER)
    
    def get_today_done_counter(self):
        return self.get_text(OrderFeedPageLocators.TODAY_DONE_COUNTER)
    
    def is_order_number_in_progress_visible(self, order_number):
        return self.is_element_visible(
            OrderFeedPageLocators.order_number_in_progress(order_number)
        )

    def wait_order_number_in_progress_visible(self, order_number):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(
                OrderFeedPageLocators.order_number_in_progress(order_number)
            )
        )
    
    def get_in_progress_orders_text(self):
        return self.get_text(OrderFeedPageLocators.IN_PROGRESS_ORDERS_LIST)