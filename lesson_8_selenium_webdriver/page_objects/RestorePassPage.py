from selenium.webdriver.common.by import By
from .BasePage import BasePage


class RestorePassPage(BasePage):
    USER_EMAIL_FIELD = (By.NAME, "email")
    SEND_EMAIL_BUTTON = (By.XPATH, "//button[text()=' Reset']")
    EMAIL_NOT_FOUND_ALERT = \
        (By.XPATH, "//div[contains(@class, 'alert') and contains(text(), 'E-Mail Address was not found')]")

    def verify_page(self, **kwargs):
        self._wait_for_located(RestorePassPage.USER_EMAIL_FIELD, **kwargs)
        return self

    def send_email(self, email):
        self._input(RestorePassPage.USER_EMAIL_FIELD, email)
        self._click(self.SEND_EMAIL_BUTTON)
        return self

    def verify_fail_result(self, **kwargs):
        self._wait_for_located(RestorePassPage.EMAIL_NOT_FOUND_ALERT, **kwargs)
        return self
