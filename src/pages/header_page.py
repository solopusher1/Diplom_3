import allure

from ..pages.base_page import BasePage
from src.locators.header_locators import HeaderLocators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderLocators

    @allure.step('Клик по кнопке "Личный кабинет" в хедере страницы')
    def click_to_personal_account_button(self):
        self.click_to_element_few_tries(self.locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "Конструктор" в хедере страницы')
    def click_to_constructor_button(self):
        self.click_to_element_few_tries(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов" в хедере страницы')
    def click_to_order_feed_button(self):
        self.click_to_element_few_tries(self.locators.ORDER_FEED_BUTTON)

    @allure.step('Ожидание кнопки "Летна заказов" в хедере страницы')
    def wait_for_order_feed_button_to_be_presenst(self):
        self.wait_presence_of_element(self.locators.ORDER_FEED_BUTTON)



