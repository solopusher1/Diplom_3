import allure

from ..pages.base_page import BasePage
from urls import PageUrls
from src.locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = PageUrls.ORDER_FEED_PAGE
        self.locators = OrderFeedPageLocators

    @allure.step('Проверка, что текущий url соответствует url страницы "Лента заказов"')
    def check_current_url(self):
        return self.wait_url_to_be(self.url)

    @allure.step('Переход на страницу "Лента заказов" по url')
    def open(self):
        self.get(self.url)

    @allure.step('Проверка видимости верхнего заказа в ленте заказов')
    def check_order_is_visible(self):
        return self.wait_for_visibility_of_element(self.locators.LAST_ORDER)

    @allure.step('Клик по верхнему заказу в ленте заказов')
    def click_to_order(self):
        self.click_to_element(self.locators.LAST_ORDER)

    @allure.step('Проверка видимости попапа с деталями заказа')
    def check_order_details_popup_is_visible(self):
        return self.wait_for_visibility_of_element(self.locators.ORDER_DETAILS_POPUP)

    @allure.step('Получить идентификатор последнего заказа(верхний в списке)')
    def get_last_order_id(self):
        return int(self.get_text_of_the_element(self.locators.LAST_ORDER_ID)[1:8])

    @allure.step('Проверка видимости счетчика заказов за все время')
    def check_all_time_order_count_is_visible(self):
        return self.wait_for_visibility_of_element(self.locators.ALL_TIME_ORDER_COUNT)

    @allure.step('Получить количество заказов за все время')
    def get_all_time_order_count(self):
        return int(self.get_text_of_the_element(self.locators.ALL_TIME_ORDER_COUNT))

    @allure.step('Проверка видимости счетчика заказов за сегодня')
    def check_today_order_count_is_visible(self):
        return self.wait_for_visibility_of_element(self.locators.TODAY_ORDER_COUNT)

    @allure.step('Получить количество заказов за сегодня')
    def get_today_order_count(self):
        return int(self.get_text_of_the_element(self.locators.TODAY_ORDER_COUNT))

    @allure.step('Проверка наличия переданного id заказа в списке "В работе"')
    def check_orders_id_is_in_work_list(self, order_id):
        return self.wait_for_text_to_be_present_in_element(self.locators.ORDER_IN_WORK, str(order_id))