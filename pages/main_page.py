import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открыть конструктор")
    def open_constructor(self):
        element = self.find_element(MainPageLocators.CONSTRUCTOR_LINK)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.click_clickable_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Открыть личный кабинет")
    def open_personal_account(self):
        self.click_clickable_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    
    @allure.step("Открыть вкладку Соусы")
    def open_sauces_tab(self):
        self.click_clickable_element(MainPageLocators.SAUCES_TAB)

    @allure.step("Открыть детальную информацию первого ингредиента")
    def open_first_ingredient_details(self):
        self.click_clickable_element(MainPageLocators.FIRST_BUN_INGREDIENT)

    @allure.step("Проверить, что детальная информация об ингредиенте открыта")
    def is_ingredient_details_opened(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Проверить, что детальная информаци об ингредиенте закрыта")
    def is_ingredient_details_closed(self):
        return self.is_element_not_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Закрыть модальное окно детальной информации")
    def close_ingredient_details(self):
        self.click_clickable_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Перетащить первую булку в конструктор")
    def drag_first_bun_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_BUN_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_ZONE,
        )

    @allure.step("Перетащить первый соус в конструктор")
    def drag_first_sauce_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_SAUCE_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_ZONE,
        )

    @allure.step("Получить счётчик первой булки")
    def get_first_bun_counter(self):
        return self.get_text(MainPageLocators.FIRST_BUN_INGREDIENT_COUNTER)

    @allure.step("Получить счётчик первого соуса")
    def get_first_sauce_counter(self):
        return self.get_text(MainPageLocators.FIRST_SAUCE_INGREDIENT_COUNTER)

    @allure.step("Кликнуть по кнопке оформления заказа")
    def click_order_button(self):
        self.click_clickable_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверить, что окно заказа открыто")
    def is_order_modal_opened(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_IDENTIFIER_TEXT)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_MODAL_NUMBER)

    @allure.step("Собрать бургер")
    def create_burger(self):
        self.drag_first_bun_to_constructor()
        self.open_sauces_tab()
        self.drag_first_sauce_to_constructor()
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_clickable_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    @allure.step("Дождаться загрузки реального номера заказа")
    def wait_order_number_loaded(self):
        self.wait_text_not_to_be_present(
            MainPageLocators.ORDER_MODAL_NUMBER,
            "9999",
            timeout=15,
        )
    
    @allure.step("Проверить, что открыта страница конструктора")
    def is_constructor_opened(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)
