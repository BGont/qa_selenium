import allure
from selenium.webdriver.common.by import By
from .AdminProductsPage import AdminProductsPage
from .BasePage import BasePage


class AdminPage(BasePage):
    LOGOUT_LINK = (By.XPATH, "//header[@id='header']//a[contains(@href, 'logout')]")
    MENU_CATALOG_LINK = (By.XPATH, "//ul[@id='menu']/li[@id='menu-catalog']/a[text()=' Catalog']")
    MENU_PRODUCTS_LINK = (By.XPATH, "//ul[@id='menu']/li[@id='menu-catalog']//a[text()='Products']")

    @allure.step("Проверка страницы администрирования")
    def verify_login(self, **kwargs):
        self._wait_for_visible(AdminPage.LOGOUT_LINK, **kwargs)
        return self

    @allure.step("Попытка перехода в каталог продуктов")
    def click_catalog_products(self):
        self._click(AdminPage.MENU_CATALOG_LINK)
        self._wait_for_clickable(AdminPage.MENU_PRODUCTS_LINK)
        self._click(AdminPage.MENU_PRODUCTS_LINK)
        return AdminProductsPage(self.driver)

    @allure.step("Выход из режима администрирования")
    def logout(self):
        self._click(AdminPage.LOGOUT_LINK)
