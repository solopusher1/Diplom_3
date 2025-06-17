import allure
from ..pages.base_page import BasePage
from urls import PageUrls
from src.locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators
        self.url = PageUrls.LOGIN_PAGE

    @allure.step('Переход на страницу авторизации по url')
    def open(self):
        self.get(self.url)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_to_password_recovery_button(self):
        self.click_to_element(self.locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Заполнить поле "Email"')
    def fill_the_email_field(self, email):
        self.filling_the_field(self.locators.EMAIL_INPUT, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_the_password_field(self, password):
        self.filling_the_field(self.locators.PASSWORD_INPUT, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_to_enter_button(self):
        self.click_to_element_few_tries(self.locators.ENTER_BUTTON)

    @allure.step('Проверка, что текущий url соответствует url страницы авторизации')
    def check_current_url(self):
        return self.wait_url_to_be(self.url)