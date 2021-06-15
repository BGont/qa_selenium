import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture(params=["/index.php?route=account/login"], scope="function")
def user_login_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_user_login_page(user_login_page_browser):
    wait = WebDriverWait(user_login_page_browser, 5, 1)

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']/div/div[1]")))
    except TimeoutException:
        raise AssertionError("Блок регистрации нового пользователя не найден")

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']/div/div[2]")))
    except TimeoutException:
        raise AssertionError("Блок входа зарегистрированного пользователя не найден")

    try:
        wait.until(EC.presence_of_element_located((By.NAME, "email")))
    except TimeoutException:
        raise AssertionError("Поле ввода e-mail не найдено")

    try:
        wait.until(EC.presence_of_element_located((By.NAME, "password")))
    except TimeoutException:
        raise AssertionError("Поле ввода пароля не найдено")

    menu_items = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//aside[@id='column-right']/div[@class='list-group']/a")))
    if len(menu_items) != 13:
        raise AssertionError("Пункты бокового меню либо частично либо полностью отсутствуют")
