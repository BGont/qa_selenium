from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: tuple, index: int):
        return self.driver.find_elements(*selector)[index]

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, context=None, wait=3, wait_freq=1):
        context = context or self.driver
        try:
            return WebDriverWait(context, wait, wait_freq).until(EC.visibility_of_element_located(selector))
        except TimeoutError:
            raise AssertionError()

    def _wait_for_located(self, selector, context=None, wait=5, wait_freq=1):
        context = context or self.driver
        try:
            return WebDriverWait(context, wait, wait_freq).until(EC.presence_of_all_elements_located(selector))
        except TimeoutError:
            raise AssertionError()

    def _wait_for_all_located(self, selector, context=None, wait=5, wait_freq=1):
        context = context or self.driver
        try:
            return WebDriverWait(context, wait, wait_freq).until(EC.presence_of_all_elements_located(selector))
        except TimeoutError:
            raise AssertionError()

    def _wait_for_all_visible(self, selector, context=None, wait=5, wait_freq=1):
        context = context or self.driver
        try:
            return WebDriverWait(context, wait, wait_freq).until(EC.visibility_of_all_elements_located(selector))
        except TimeoutError:
            raise AssertionError()

    def _wait_for_clickable(self, selector, context=None, wait=5, wait_freq=1):
        context = context or self.driver
        try:
            return WebDriverWait(context, wait, wait_freq).until(EC.element_to_be_clickable(selector))
        except TimeoutError:
            raise AssertionError()

    def _get_element_text(self, selector, index):
        return self.__element(selector, index).text
