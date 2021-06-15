import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture(params=["/index.php?route=product/product&path=57&product_id=49"], scope="function")
def card_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_card_page(card_page_browser):
    wait = WebDriverWait(card_page_browser, 5, 1)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))
    except TimeoutException:
        raise AssertionError("Название товара не найдено")

    try:
        wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "#content ul.thumbnails > li.image-additional > a.thumbnail > img")))
    except TimeoutException:
        raise AssertionError("Дополнительные миниатюры товара не найдены или не видны")

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))
    except TimeoutException:
        raise AssertionError("Кнопка Add to cart не найдена")

    try:
        wait.until(EC.visibility_of_element_located((By.NAME, "quantity")))
    except TimeoutException:
        raise AssertionError("Поле выбора количества товаров для добавления в корзину отсутсвует")

    try:
        wait.until(EC.visibility_of_element_located((By.ID, "tab-description")))
    except TimeoutException:
        raise AssertionError("Описание товара не найдено")
