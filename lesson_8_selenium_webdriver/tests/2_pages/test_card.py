import pytest
from page_objects import ProductPage


@pytest.fixture(params=["/index.php?route=product/product&path=57&product_id=49"], scope="function")
def card_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_card_page(card_page_browser):
    ProductPage(card_page_browser) \
        .verify_product_name() \
        .verify_thumbnails() \
        .verify_add_to_cart_button() \
        .verify_quantity_form_field() \
        .verify_product_description()
