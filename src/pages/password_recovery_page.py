import allure
from ..pages.base_page import BasePage
from src.locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from urls import PageUrls


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryPageLocators
        self.url = PageUrls.PASSWORD_RECOVERY_PAGE

    @allure.step('Переход на страницу "Восстановление пароля" по url')
    def open(self):
        self.get(self.url)

    @allure.step('Проверка, что текущий url соответствует url страницы "Восстановление пароля"')
    def check_current_url(self):
        return self.wait_url_to_be(self.url)

    @allure.step('Заполнить поле Email')
    def fill_email_field(self, email):
        self.filling_the_field(self.locators.EMAIL_FIELD, email)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_to_recovery_button(self):
        self.click_to_element(self.locators.RECOVERY_BUTTON)