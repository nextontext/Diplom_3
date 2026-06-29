from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    def open_profile(self):
        self.click_clickable_element(ProfilePageLocators.PROFILE_BUTTON)

    def open_order_history(self):
        self.click_clickable_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    def logout(self):
        self.click_clickable_element(ProfilePageLocators.LOGOUT_BUTTON)

    def get_first_order_number_from_history(self):
        return self.get_text(ProfilePageLocators.FIRST_ORDER_NUMBER_IN_HISTORY)
