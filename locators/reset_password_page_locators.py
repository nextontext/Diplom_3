from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (
        By.XPATH,
        "//input[@name='Введите новый пароль']/following-sibling::div",
    )
    PASSWORD_INPUT_CONTAINER = (
        By.XPATH,
        "//input[@name='Введите новый пароль']/ancestor::div[contains(@class, 'input_type_password')]",
    )