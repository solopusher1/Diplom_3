import allure

from src.locators.main_page_locators import MainPageLocators
from ..pages.base_page import BasePage
from urls import PageUrls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = PageUrls.HOME_PAGE
        self.locators = MainPageLocators

    @allure.step('Проверка видимости заголовка "Соберите бургер"')
    def check_visibility_of_make_burger_header(self):
        return self.wait_for_visibility_of_element(self.locators.HEADER_MAKE_YOUR_BURGER)

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self):
        return self.click_to_element(self.locators.RANDOM_INGREDIENT)

    @allure.step('Проверка видимости заголовка попапа "Детали ингредиента"')
    def check_visibility_of_ingredient_details_header(self):
        return self.wait_for_visibility_of_element(self.locators.INGREDIENT_DETAILS_POPUP_HEADER)

    @allure.step('Проверка отсутствия заголовка попапа "Детали ингредиента"')
    def check_invisibility_of_ingredient_details_header(self):
        return self.wait_for_invisibility_of_element(self.locators.INGREDIENT_DETAILS_POPUP_HEADER)

    @allure.step('Клик по крестику на попапе "Детали ингредиента"')
    def click_to_popup_close_button(self):
        return self.click_to_element(self.locators.INGREDIENT_DETAILS_POPUP_CLOSE_BUTTON)

    @allure.step('Перетаскивание ингредиента в поле конструктора')
    def move_ingredient_to_constructor_field(self):
        source_locator = self.locators.RANDOM_INGREDIENT
        dest_locator = self.locators.BURGER_CONSTRUCTOR_SECTION
        self.drag_and_drop(source_locator, dest_locator)

    @allure.step('Получить текущее количество ингредиента из его каунтера')
    def get_current_ingredient_quantity(self):
        return int(self.get_text_of_the_element(self.locators.RANDOM_INGREDIENT_COUNTER))

    @allure.step('Проверка видимости идентификатора заказа')
    def check_visibility_of_order_id(self):
        return self.wait_for_visibility_of_element(self.locators.ORDER_ID)

    @allure.step('Получить идентификатор заказа')
    def get_order_id(self):
        return int(self.get_text_of_the_element(self.locators.ORDER_ID))

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_to_make_order_button(self):
        return self.click_to_element_few_tries(self.locators.MAKE_ORDER_BUTTON)

    @allure.step('Проверка видимости ингредиента')
    def check_visibility_of_ingredient(self):
        return self.wait_for_visibility_of_element(self.locators.RANDOM_INGREDIENT)

    @allure.step('Ждем, когда пропадет анимация загрузки страницы')
    def wait_for_invisibility_of_loading_page_animation(self):
        return self.wait_for_invisibility_of_element(self.locators.LOADING_PAGE_ANIMATION)

    @allure.step('Ждем, когда появится анимация загрузки страницы')
    def wait_for_visibility_of_loading_page_animation(self):
        return self.wait_for_visibility_of_element(self.locators.LOADING_PAGE_ANIMATION)

    @allure.step('Клик по крестику на попапе "Заказ оформлен"')
    def click_to_close_button_of_order_was_placed_popup(self):
        return self.click_to_element_few_tries(self.locators.ORDER_WAS_PLACED_POPUP_CLOSE_BUTTON)