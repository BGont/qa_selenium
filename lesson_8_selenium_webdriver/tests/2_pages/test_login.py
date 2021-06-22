import pytest
from page_objects import UserLoginPage


@pytest.fixture(params=["/index.php?route=account/login"], scope="function")
def user_login_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_user_login_page(user_login_page_browser):
    UserLoginPage(user_login_page_browser) \
        .verify_registration_block() \
        .verify_login_block() \
        .verify_email_field() \
        .verify_password_field() \
        .verify_right_menu_items()
