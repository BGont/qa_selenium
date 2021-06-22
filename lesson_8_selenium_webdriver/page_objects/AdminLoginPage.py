import allure
from selenium.webdriver.common.by import By
from .AdminPage import AdminPage
from .BasePage import BasePage
from .RestorePassPage import RestorePassPage


class AdminLoginPage(BasePage):
    LOGIN_INVITATION = (By.XPATH, "//h1[text()=' Please enter your login details.']")
    LOGIN_EMAIL = (By.NAME, "username")
    LOGIN_PASSWORD = (By.NAME, "password")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login']")

    def verify_page(self):
        return self.verify_log_in_invitation(wait=10)

    @allure.step("Проверка наличия приглашения для ввода аутентификационных данных")
    def verify_log_in_invitation(self, **kwargs):
        self._wait_for_located(AdminLoginPage.LOGIN_INVITATION, **kwargs)
        return self

    @allure.step("Проверка наличия поля ввода e-mail")
    def verify_login_email_field(self, **kwargs):
        self._wait_for_located(AdminLoginPage.LOGIN_EMAIL, **kwargs)
        return self

    @allure.step("Проверка наличия поля ввода пароля")
    def verify_login_password_field(self, **kwargs):
        self._wait_for_located(AdminLoginPage.LOGIN_PASSWORD, **kwargs)
        return self

    @allure.step("Проверка наличия ссылки для восстановления пароля")
    def verify_forgotten_password_link(self, **kwargs):
        self._wait_for_located(AdminLoginPage.FORGOTTEN_PASSWORD_LINK, **kwargs)
        return self

    @allure.step("Проверка наличия кнопки для отправки данных формы аутентификации")
    def verify_login_button(self, **kwargs):
        self._wait_for_clickable(AdminLoginPage.LOGIN_BUTTON, **kwargs)
        return self

    @allure.step("Попытка залогиниться с ролью администратора")
    def login_user(self, email, password):
        self._input(self.LOGIN_EMAIL, email)
        self._input(self.LOGIN_PASSWORD, password)
        self._click(self.LOGIN_BUTTON)

        return AdminPage(self.driver)

    @allure.step("Попытка перехода по ссылке для восстановления пароля")
    def click_forgotten_password(self):
        self._click(self.FORGOTTEN_PASSWORD_LINK)
        return RestorePassPage(self.driver)
