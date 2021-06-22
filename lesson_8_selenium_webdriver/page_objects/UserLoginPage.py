from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserLoginPage(BasePage):
    REGISTRATION_BLOCK = (By.XPATH, "//div[@id='content']/div/div[1]")
    LOGIN_FORM = (By.XPATH, "//div[@id='content']/div/div[2]")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    RIGHT_MENU_ITEMS = (By.XPATH, "//aside[@id='column-right']/div[@class='list-group']/a")

    def verify_registration_block(self, **kwargs):
        self._wait_for_located(UserLoginPage.REGISTRATION_BLOCK, **kwargs)
        return self

    def verify_login_block(self, **kwargs):
        self._wait_for_located(UserLoginPage.LOGIN_FORM, **kwargs)
        return self

    def verify_email_field(self, **kwargs):
        self._wait_for_located(UserLoginPage.EMAIL_FIELD, **kwargs)
        return self

    def verify_password_field(self, **kwargs):
        self._wait_for_located(UserLoginPage.PASSWORD_FIELD, **kwargs)
        return self

    def verify_right_menu_items(self, **kwargs):
        self._wait_for_located(UserLoginPage.RIGHT_MENU_ITEMS, **kwargs)
        return self
