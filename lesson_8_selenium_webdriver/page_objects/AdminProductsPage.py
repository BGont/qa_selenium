from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminProductsPage(BasePage):
    PRODUCTS_TABLE = (By.XPATH, "//div[@id='content']/div[@class='container-fluid']/div[@class='row']/div[2]//table")

    def verify_page(self, **kwargs):
        self._wait_for_located(AdminProductsPage.PRODUCTS_TABLE, **kwargs)
        return self
