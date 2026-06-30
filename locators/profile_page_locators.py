from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")
    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[@href='/account/order-history' and text()='История заказов']",
    )
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    FIRST_ORDER_NUMBER_IN_HISTORY = (
        By.XPATH,
        "(//a[contains(@href, '/account/order-history/')]//p[contains(text(), '#')])[1]",
    )
