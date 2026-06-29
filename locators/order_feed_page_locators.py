from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FIRST_ORDER = (
        By.XPATH,
        "(//ul[contains(@class, 'OrderFeed_list')]//a[contains(@class, 'OrderHistory_link')])[1]",
    )
    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_orderBox')]",
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//div[contains(@class, 'Modal_orderBox')]//p[contains(text(), '#')]",
    )
    ORDER_MODAL_COMPOSITION_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Modal_orderBox')]//p[text()='Cостав']",
    )

    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )

    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )

    IN_PROGRESS_ORDERS_LIST = (
        By.XPATH,
        "//p[contains(text(), 'В работе')]/following-sibling::ul",
    )

    @staticmethod
    def order_number_in_feed(order_number):
        return (
            By.XPATH,
            f"//ul[contains(@class, 'OrderFeed_list')]//p[text()='{order_number}']",
        )
    
    @staticmethod
    def order_number_in_progress(order_number):
        return (
            By.XPATH,
            f"//*[contains(normalize-space(), 'В работе')]/following::ul[1]//li[contains(., '{order_number}')]",
        )