import allure

from src.pages.login_page import LoginPage
from src.pages.header_page import HeaderPage
from src.pages.main_page import MainPage
from src.pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title('Проверка, что при клике на заказ на странице "Лента заказов" открывается всплывающее окно с деталями заказа')
    @allure.description('Открываем страницу "Лента заказов", кликаем на последний заказ, проверяем наличие попапа')
    def test_click_to_order_open_order_details_popup(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        order_feed_page.check_order_is_visible()
        order_feed_page.click_to_order()

        assert order_feed_page.check_order_details_popup_is_visible(), "Попап не появился"

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Создаем заказ, сверяем его id с id последнего заказа в ленте заказов')
    def test_new_orders_are_displayed_in_order_feed(self, driver, user):
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
        main_page.wait_for_invisibility_of_loading_page_animation()
        order_id = main_page.get_order_id()
        main_page.click_to_close_button_of_order_was_placed_popup()
        header_page = HeaderPage(driver)
        header_page.click_to_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.check_order_is_visible()
        last_order_id = order_feed_page.get_last_order_id()

        assert order_id == last_order_id, "ID заказов не совпадают"

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Проверяем счетчик, создаем новый заказ, проверяем, что счетчик прибавил один заказ')
    def test_all_time_order_counter_increases_when_new_order_is_created(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open()
        email, password = user
        login_page.fill_the_email_field(email)
        login_page.fill_the_password_field(password)
        login_page.click_to_enter_button()
        header_page = HeaderPage(driver)
        header_page.click_to_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.check_all_time_order_count_is_visible()
        order_count = order_feed_page.get_all_time_order_count()
        header_page.click_to_constructor_button()
        main_page = MainPage(driver)
        main_page.check_visibility_of_ingredient()
        main_page.move_ingredient_to_constructor_field()
        main_page.click_to_make_order_button()
        main_page.wait_for_invisibility_of_loading_page_animation()
        main_page.click_to_close_button_of_order_was_placed_popup()
        header_page.click_to_order_feed_button()
        order_feed_page.check_all_time_order_count_is_visible()
        new_order_count = order_feed_page.get_all_time_order_count()

        assert new_order_count == order_count + 1, "Не произошло увеличение счетчика на 1 заказ"

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Проверяем счетчик, создаем новый заказ, проверяем, что счетчик прибавил один заказ')
    def test_today_order_counter_increases_when_new_order_is_created(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open()
        email, password = user
        login_page.fill_the_email_field(email)
        login_page.fill_the_password_field(password)
        login_page.click_to_enter_button()
        header_page = HeaderPage(driver)
        header_page.click_to_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.check_today_order_count_is_visible()
        order_count = order_feed_page.get_today_order_count()
        header_page.click_to_constructor_button()
        main_page = MainPage(driver)
        main_page.check_visibility_of_ingredient()
        main_page.move_ingredient_to_constructor_field()
        main_page.click_to_make_order_button()
        main_page.wait_for_invisibility_of_loading_page_animation()
        main_page.click_to_close_button_of_order_was_placed_popup()
        header_page.click_to_order_feed_button()
        order_feed_page.check_today_order_count_is_visible()
        new_order_count = order_feed_page.get_today_order_count()

        assert new_order_count == order_count + 1, "Не произошло увеличение счетчика на 1 заказ"

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('Создаем заказ, проверяем, что его номер появился в разделе "В работе"')
    def test_new_orders_id_appears_in_section_at_work(self, driver, user):
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
        main_page.wait_for_invisibility_of_loading_page_animation()
        order_id = main_page.get_order_id()
        main_page.click_to_close_button_of_order_was_placed_popup()
        header_page = HeaderPage(driver)
        header_page.click_to_order_feed_button()
        order_feed_page = OrderFeedPage(driver)

        assert order_feed_page.check_orders_id_is_in_work_list(order_id), "ID заказа не появился в разделе 'В работе'"