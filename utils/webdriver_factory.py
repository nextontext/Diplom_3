from selenium import webdriver


class WebDriverFactory:

    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()

        if browser_name == "chrome":
            return webdriver.Chrome()

        raise ValueError(f"Unsupported browser: {browser_name}")
