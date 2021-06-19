import pytest
from page_objects import MainPage


@pytest.fixture(params=["/"], scope="function")
def main_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_main_page(main_page_browser):
    MainPage(main_page_browser) \
        .verify_top_menu() \
        .verify_cart() \
        .verify_featured_products() \
        .verify_logo() \
        .verify_footer()
