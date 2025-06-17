import allure
from ..pages.base_page import BasePage
from src.locators.reset_password_page_locators import ResetPasswordPageLocators
from urls import PageUrls

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = PageUrls.RESET_PASSWORD_PAGE
        self.locators = ResetPasswordPageLocators


    @allure.step('Проверка, что текущий url соответствует url страницы "Сброс пароля"')
    def check_current_url(self):
        return self.wait_url_to_be(self.url)

    @allure.step('Клик на кнопку "показать/скрыть пароль"')
    def click_to_show_password_button(self):
        self.click_to_element_few_tries(self.locators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем, что кнопка "показать/скрыть пароль" кликабельна')
    def check_show_password_button_is_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем, что поле "Пароль" активно (подсвечено)')
    def check_password_field_is_active(self):
        return self.wait_for_visibility_of_element(self.locators.PASSWORD_FIELD_ACTIVE)