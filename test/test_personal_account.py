import allure

from src.pages.login_page import LoginPage
from src.pages.header_page import HeaderPage
from src.pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода на страницу личного кабинета по кнопке «Личный кабинет» (для авторизованного пользователя)')
    @allure.description('Авторизуемся, кликаем по кнопке "Личный кабинет" в хедере, сверяем текущий url с ожидаемым')
    def test_click_to_personal_account_button_authorized_user_open_personal_account_page(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open()
        email, password = user
        login_page.fill_the_email_field(email)
        login_page.fill_the_password_field(password)
        login_page.click_to_enter_button()

        header_page = HeaderPage(driver)
        header_page.click_to_personal_account_button()

        personal_account_page = PersonalAccountPage(driver)

        assert personal_account_page.check_current_url(), "Урл не соответствует ожидаемому значению"

    @allure.title('Проверка перехода в раздел «История заказов» (для авторизованного пользователя)')
    @allure.description('Авторизуемся, в разделе "Личный кабинет" кликаем "История заказов", сверяем текущий url с ожидаемым')
    def test_click_to_order_history_button_authorized_user_open_order_history_page(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open()
        email, password = user
        login_page.fill_the_email_field(email)
        login_page.fill_the_password_field(password)
        login_page.click_to_enter_button()
        header_page = HeaderPage(driver)
        header_page.click_to_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.check_order_history_button_is_clickable()
        personal_account_page.click_to_order_history_button()

        assert personal_account_page.check_url_to_be_order_history_url(), "Урл не соответствует ожидаемому значению"

    @allure.title('Проверка выхода из аккаунта (для авторизованного пользователя)')
    @allure.description('Авторизуемся, в разделе "Личный кабинет" кликаем "Выход", сверяем текущий url с ожидаемым')
    def test_click_to_logout_button_authorized_user_open_login_page(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open()
        email, password = user
        login_page.fill_the_email_field(email)
        login_page.fill_the_password_field(password)
        login_page.click_to_enter_button()
        header_page = HeaderPage(driver)
        header_page.click_to_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.check_logout_button_is_clickable()
        personal_account_page.click_to_logout_button()
        login_page = LoginPage(driver)

        assert login_page.check_current_url(), "Урл не соответствует ожидаемому значению"