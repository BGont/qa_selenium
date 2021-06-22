import allure
import pytest
from page_objects import AdminPage, AdminLoginPage


@pytest.fixture(params=["/admin/"], scope="function")
def admin_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


# default docker opencart admin credentials
@pytest.fixture
def admin_credentials():
    return "user", "bitnami"


@pytest.fixture
def unregistered_user_email():
    return "test@test.test"


@allure.title("Проверка страницы входа с административными правами")
def test_admin_login_page(admin_page_browser):
    AdminLoginPage(admin_page_browser) \
        .verify_log_in_invitation() \
        .verify_login_email_field() \
        .verify_login_password_field() \
        .verify_forgotten_password_link() \
        .verify_login_button()


@allure.title("Проверка перехода в административный каталог продуктов")
def test_admin_products(admin_page_browser, admin_credentials):
    AdminLoginPage(admin_page_browser) \
        .login_user(*admin_credentials) \
        .verify_login(wait=10) \
        .click_catalog_products() \
        .verify_page(wait=10)
    AdminPage(admin_page_browser).logout()


@allure.title("Проверка восстановления пароля незарегистрированного пользователя")
def test_restore_password(admin_page_browser, unregistered_user_email):
    password_restore_page = AdminLoginPage(admin_page_browser).click_forgotten_password()
    password_restore_page. \
        verify_page(wait=10). \
        send_email(unregistered_user_email) \
        .verify_fail_result()
