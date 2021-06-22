from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    TOP_MENU = (By.CSS_SELECTOR, "#menu ul.navbar-nav")
    CART = (By.ID, "cart")
    FEATURED_PRODUCTS = (By.XPATH, "//h3[text()='Featured']/following-sibling::div[@class='row']")
    LOGO = (By.XPATH, "//*[@id=\"logo\"]")
    FOOTER = (By.CSS_SELECTOR, "footer")

    def verify_top_menu(self, **kwargs):
        self._wait_for_located(MainPage.TOP_MENU, **kwargs)
        return self

    def verify_cart(self, **kwargs):
        self._wait_for_located(MainPage.CART, **kwargs)
        return self

    def verify_featured_products(self, **kwargs):
        self._wait_for_located(MainPage.FEATURED_PRODUCTS, **kwargs)
        return self

    def verify_logo(self, **kwargs):
        self._wait_for_located(MainPage.LOGO, **kwargs)
        return self

    def verify_footer(self, **kwargs):
        self._wait_for_located(MainPage.FOOTER, **kwargs)
        return self
