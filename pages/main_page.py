from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):

    def open_constructor(self):
        element = self.find_element(MainPageLocators.CONSTRUCTOR_LINK)
        self.driver.execute_script("arguments[0].click();", element)

    def open_order_feed(self):
        self.click_clickable_element(MainPageLocators.ORDER_FEED_LINK)

    def open_personal_account(self):
        self.click_clickable_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    
    def open_sauces_tab(self):
        self.click_clickable_element(MainPageLocators.SAUCES_TAB)

    def open_first_ingredient_details(self):
        self.click_clickable_element(MainPageLocators.FIRST_BUN_INGREDIENT)

    def is_ingredient_details_opened(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    def is_ingredient_details_closed(self):
        return self.is_element_not_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    def close_ingredient_details(self):
        self.click_clickable_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def drag_first_bun_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_BUN_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_ZONE,
        )

    def drag_first_sauce_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_SAUCE_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_ZONE,
        )

    def get_first_bun_counter(self):
        return self.get_text(MainPageLocators.FIRST_BUN_INGREDIENT_COUNTER)

    def get_first_sauce_counter(self):
        return self.get_text(MainPageLocators.FIRST_SAUCE_INGREDIENT_COUNTER)

    def click_order_button(self):
        self.click_clickable_element(MainPageLocators.ORDER_BUTTON)

    def is_order_modal_opened(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_IDENTIFIER_TEXT)

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_MODAL_NUMBER)

    def create_burger(self):
        self.drag_first_bun_to_constructor()
        self.open_sauces_tab()
        self.drag_first_sauce_to_constructor()
    
    def close_order_modal(self):
        self.click_clickable_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    def wait_order_number_loaded(self):
        WebDriverWait(self.driver, 15).until_not(
            expected_conditions.text_to_be_present_in_element(
                MainPageLocators.ORDER_MODAL_NUMBER,
                "9999",
            )
        )
    
    def is_constructor_opened(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)