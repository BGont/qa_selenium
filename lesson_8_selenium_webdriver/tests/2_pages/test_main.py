import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture(params=["/"], scope="function")
def main_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_main_page(main_page_browser):
    wait = WebDriverWait(main_page_browser, 5, 1)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu ul.navbar-nav")))
    except TimeoutException:
        raise AssertionError("Горизонтальное меню не найдено")

    try:
        wait.until(EC.presence_of_element_located((By.ID, "cart")))
    except TimeoutException:
        raise AssertionError("Корзина не найдена")

    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h3[text()='Featured']/following-sibling::div[@class='row']")))
    except TimeoutException:
        raise AssertionError("Карусель featured продуктов не найдена")

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"logo\"]")))
    except TimeoutException:
        raise AssertionError("Логотип не найден")

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))
    except TimeoutException:
        raise AssertionError("Подвал не найден")
