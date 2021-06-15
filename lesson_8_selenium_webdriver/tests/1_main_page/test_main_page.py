import pytest


@pytest.fixture(params=["/"], scope="function")
def app_browser(request, browser):
    browser.get(browser.url + request.param)
    return browser


def test_title(app_browser):
    main_page_title = "Your Store"
    assert app_browser.title == main_page_title
