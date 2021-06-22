import pytest
from page_objects import CatalogPage


@pytest.fixture(params=["/index.php?route=product/category&path=20"], scope="function")
def catalog_page_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_catalog_page(catalog_page_browser):
    CatalogPage(catalog_page_browser) \
        .verify_breadcrumbs_block() \
        .verify_products_compare_link() \
        .verify_banners() \
        .verify_products() \
        .verify_products_images()
