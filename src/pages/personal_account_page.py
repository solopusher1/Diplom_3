import allure
from ..pages.base_page import BasePage
from src.locators.personal_account_page_locators import PersonalAccountPageLocators
from urls import PageUrls

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountPageLocators
        self.url = PageUrls.PERSONAL_ACCOUNT_PAGE

    @allure.step('Проверка, что текущий url соответствует url страницы "Личный кабинет"')
    def check_current_url(self):
        return self.wait_url_to_be(self.url)

    @allure.step('Клик по кнопке "История заказов"')
    def click_to_order_history_button(self):
        self.click_to_element_few_tries(self.locators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка, что текущий url соответствует url страницы "История заказов"')
    def check_url_to_be_order_history_url(self):
        return self.wait_url_to_be(PageUrls.ORDER_HISTORY_PAGE)

    @allure.step('Проверка, что кнопка "История заказов" кликабельна')
    def check_order_history_button_is_clickable(self):
        return self.wait_for_element_to_be_clickable(self.locators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка, что кнопка "Выход" кликабельна')
    def check_logout_button_is_clickable(self):
        return self.wait_for_element_to_be_clickable(self.locators.LOGOUT_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_to_logout_button(self):
        self.click_to_element_few_tries(self.locators.LOGOUT_BUTTON)