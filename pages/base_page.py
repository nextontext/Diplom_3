import allure

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Кликнуть по кликабельному элементу")
    def click_clickable_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

        # Защита от падений в firefox при клике
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Получить значение атрибута элемента")
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step("Проверить, что элемент отображается")
    def is_element_visible(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Дождаться, что URL содержит нужный путь")
    def wait_url_contains(self, url_part):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(url_part)
        )
    
    @allure.step("Проверить, что элемент не отображается")
    def is_element_not_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
    
    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        js_script = """
            function simulateDragDrop(sourceNode, targetNode) {
                var EVENT_TYPES = {
                    DRAG_END: 'dragend',
                    DRAG_START: 'dragstart',
                    DROP: 'drop',
                    DRAG_OVER: 'dragover'
                };

                function createCustomEvent(type) {
                    var event = new CustomEvent("CustomEvent");
                    event.initCustomEvent(type, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(type, val) {
                            this.data[type] = val;
                        },
                        getData: function(type) {
                            return this.data[type];
                        }
                    };
                    return event;
                }

                function dispatchEvent(node, type, event) {
                    if (node.dispatchEvent) {
                        return node.dispatchEvent(event);
                    }
                    if (node.fireEvent) {
                        return node.fireEvent("on" + type, event);
                    }
                }

                var event = createCustomEvent(EVENT_TYPES.DRAG_START);
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event);

                var dragOverEvent = createCustomEvent(EVENT_TYPES.DRAG_OVER);
                dragOverEvent.dataTransfer = event.dataTransfer;
                dispatchEvent(targetNode, EVENT_TYPES.DRAG_OVER, dragOverEvent);

                var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
                dropEvent.dataTransfer = event.dataTransfer;
                dispatchEvent(targetNode, EVENT_TYPES.DROP, dropEvent);

                var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
                dragEndEvent.dataTransfer = event.dataTransfer;
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
            }

            simulateDragDrop(arguments[0], arguments[1]);
        """

        self.driver.execute_script(js_script, source, target)

    @allure.step("Дождаться точного URL")
    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(url)
        )
    
    @allure.step("Дождаться видимости элемента")
    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться, что текст пропал из элемента")
    def wait_text_not_to_be_present(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url