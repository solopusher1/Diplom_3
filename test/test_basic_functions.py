import allure
from src.pages.login_page import LoginPage
from src.pages.header_page import HeaderPage
from src.pages.main_page import MainPage
from src.pages.order_feed_page import OrderFeedPage


class TestBasicFunctions:

    @allure.title('Проверка перехода на главную страницу по кнопке «Конструктор»')
    @allure.description('Открываем страницу авторизации, кликаем на "Конструктор", проверяем наличие заголовка')
    def test_click_to_constructor_button_open_home_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        header_page = HeaderPage(driver)
        header_page.click_to_constructor_button()
        main_page = MainPage(driver)

        assert main_page.check_visibility_of_make_burger_header(), "Заголовок не найден"

    @allure.title('Проверка перехода на страницу "Лента заказов" по кнопке "Лента заказов"')
    @allure.description('Открываем страницу авторизации, кликаем на "Лента заказов", сверяем текущий url с ожидаемым')
    def test_click_to_order_feed_button_open_order_feed_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        header_page = HeaderPage(driver)
        header_page.click_to_order_feed_button()
        order_feed_page = OrderFeedPage(driver)

        assert order_feed_page.check_current_url(), "Урл не соответствует ожидаемому значению"

    @allure.title('Проверка, что по клику на ингредиент появляется попап "Детали ингредиента"')
    @allure.description('Открываем главную страницу, кликаем на ингредиент, проверяем наличие заголовка попапа')
    def test_click_to_ingredient_open_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()

        assert main_page.check_visibility_of_ingredient_details_header(), "Элемент отсутствует"

    @allure.title('Проверка закрытия попапа "Детали ингредиента" при нажатии на крестик')
    @allure.description('Кликаем на ингредиент, закрываем попап "Детали ингредиента", проверяем отсутствие заголовка попапа')
    def test_click_to_popup_close_button_close_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        main_page.click_to_popup_close_button()

        assert main_page.check_invisibility_of_ingredient_details_header(), "Элемент присутствует"

    @allure.title('Проверка, что при добавлении ингредиента в заказ увеличивается каунтер данного ингредиента')
    @allure.description('Перетаскиваем ингредиент на поле конструктора, проверяем каунтер')
    def test_add_ingredient_increase_its_quantity_in_counter(self, driver):
        main_page = MainPage(driver)
        num_1 = main_page.get_current_ingredient_quantity()
        main_page.move_ingredient_to_constructor_field()
        num_2 = main_page.get_current_ingredient_quantity()

        assert num_2 > num_1, "Количество в каунтере не увеличилось"

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('Авторизуемся, добавляем ингредиент, кликаем "Оформить заказ", проверяем наличие надписи "идентификатор заказа"')
    def test_authorized_user_is_able_to_make_order(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open()
        email, password = user
        login_page.fill_the_email_field(email)
        login_page.fill_the_password_field(password)
        login_page.click_to_enter_button()
        main_page = MainPage(driver)
        main_page.check_visibility_of_ingredient()
        main_page.move_ingredient_to_constructor_field()
        main_page.click_to_make_order_button()

        assert main_page.check_visibility_of_order_id(), "ID заказа не отображается"