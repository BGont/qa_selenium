from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):
    BREADCRUMBS_BLOCK = (By.CLASS_NAME, "breadcrumb")
    PRODUCTS_COMPARE_LINK = (By.CSS_SELECTOR, "#content a#compare-total")
    BANNERS = (By.XPATH, '//aside[@id="column-left"]/div[@class="swiper-viewport"]//img')
    PRODUCTS = (By.CSS_SELECTOR, "#content div.product-layout.product-grid")
    PRODUCT_IMG = (By.XPATH, '//div[@class="product-thumb"]/div/a/img')

    def verify_breadcrumbs_block(self, **kwargs):
        self._wait_for_located(CatalogPage.BREADCRUMBS_BLOCK, **kwargs)
        return self

    def verify_products_compare_link(self, **kwargs):
        self._wait_for_located(CatalogPage.PRODUCTS_COMPARE_LINK, **kwargs)
        return self

    def verify_banners(self, **kwargs):
        self._wait_for_all_visible(CatalogPage.BANNERS, **kwargs)
        return self

    def get_products(self, **kwargs):
        return self.driver.find_elements(*CatalogPage.PRODUCTS, **kwargs)

    def verify_products(self):
        assert len(self.get_products()), "Продукты не найдены"
        return self

    def verify_products_images(self):
        missed = 0
        for product in self.get_products():
            if not self._wait_for_all_visible(CatalogPage.BANNERS, context=product):
                missed += 1
        if missed:
            raise AssertionError(f"Для {missed} продуктов отсутствуют фотографии")

        return self
