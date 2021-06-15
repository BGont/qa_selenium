import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture(params=["/index.php?route=product/category&path=20"], scope="function")
def catalog_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_catalog_page(catalog_page_browser):
    wait = WebDriverWait(catalog_page_browser, 5, 1)
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "breadcrumb")))
    except TimeoutException:
        raise AssertionError("Хлебные крошки не найдены")

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content a#compare-total")))
    except TimeoutException:
        raise AssertionError("Ссылка на сравнение продуктов отсутствует")

    try:
        wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//aside[@id="column-left"]/div[@class="swiper-viewport"]//img')))
    except TimeoutException:
        raise AssertionError("Баннеры не найдены")

    try:
        product_layouts = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content div.product-layout.product-grid")))
    except TimeoutException:
        raise AssertionError("Ни одного товара не найдено")

    try:
        for product in product_layouts:
            wait = WebDriverWait(product, 3, 1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="product-thumb"]/div/a/img')))
    except TimeoutException:
        raise AssertionError("Некоторые фотографии товаров отсутствуют")
