from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content h1")
    PRODUCT_DESCRIPTION = (By.ID, "tab-description")
    THUMBNAILS_IMAGES = (By.CSS_SELECTOR, "#content ul.thumbnails > li.image-additional > a.thumbnail > img")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[id='button-cart']")
    QUANTITY_FORM_FIELD = (By.NAME, "quantity")

    def verify_product_name(self, **kwargs):
        self._wait_for_located(ProductPage.PRODUCT_NAME, **kwargs)
        return self

    def verify_thumbnails(self, **kwargs):
        self._wait_for_all_visible(ProductPage.THUMBNAILS_IMAGES, **kwargs)
        return self

    def verify_add_to_cart_button(self, **kwargs):
        self._wait_for_located(ProductPage.ADD_TO_CART_BUTTON, **kwargs)
        return self

    def verify_quantity_form_field(self, **kwargs):
        self._wait_for_visible(ProductPage.QUANTITY_FORM_FIELD, **kwargs)
        return self

    def verify_product_description(self, **kwargs):
        self._wait_for_visible(ProductPage.PRODUCT_DESCRIPTION, **kwargs)
        return self
