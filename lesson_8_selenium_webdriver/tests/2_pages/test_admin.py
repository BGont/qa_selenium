import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture(params=["/admin/"], scope="function")
def admin_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_admin_login_page(admin_page_browser):
    wait = WebDriverWait(admin_page_browser, 5, 1)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()=' Please enter your login details.']")))
    except TimeoutException:
        raise AssertionError("Приглашение формы входа не найдено")

    try:
        wait.until(EC.presence_of_element_located((By.NAME, "username")))
    except TimeoutException:
        raise AssertionError("Поле ввода имени пользователя не найдено")

    try:
        wait.until(EC.presence_of_element_located((By.NAME, "password")))
    except TimeoutException:
        raise AssertionError("Поле ввода пароля не найдено")

    try:
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Forgotten Password")))
    except TimeoutException:
        raise AssertionError("Ссылка на восстановление пароля не найдена")

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login']")))
    except TimeoutException:
        raise AssertionError("Кнопка отправки данных формы входа не доступна")


def test_admin_products(admin_page_browser):
    admin_page_browser.find_element(By.NAME, "username").clear()
    admin_page_browser.find_element(By.NAME, "username").send_keys("user")
    admin_page_browser.find_element(By.NAME, "password").clear()
    admin_page_browser.find_element(By.NAME, "password").send_keys("bitnami")
    admin_page_browser.find_element(By.XPATH, "//button[text()=' Login']").click()

    wait = WebDriverWait(admin_page_browser, 10, 1)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Logout']")))
    except TimeoutException:
        raise AssertionError("Войти под админом не получилось")

    try:
        wait = WebDriverWait(admin_page_browser, 1)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[@id='menu']/li[@id='menu-catalog']/a[text()=' Catalog']"))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[@id='menu']/li[@id='menu-catalog']//a[text()='Products']"))).click()
        wait = WebDriverWait(admin_page_browser, 10, 1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='content']/div[@class='container-fluid']/div[@class='row']/div[2]//table")))
    except TimeoutException:
        raise AssertionError("Переход к разделу с товарами")

    try:
        wait = WebDriverWait(admin_page_browser, 1)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//header[@id='header']//a[contains(@href, 'logout')]"))).click()
    except TimeoutException:
        raise AssertionError("Выйти не удалось")


def test_restore_password(admin_page_browser):
    wait = WebDriverWait(admin_page_browser, 3, 1)
    admin_page_browser.find_element(By.LINK_TEXT, "Forgotten Password").click()
    email_form_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_form_field.clear()
    email_form_field.send_keys("test@test.ru")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Reset']"))).click()
    wait = WebDriverWait(admin_page_browser, 10, 1)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'alert') and contains(text(), 'E-Mail Address was not found')]")))
