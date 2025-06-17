import allure

from helpers import *
from src.pages.login_page import LoginPage
from src.pages.password_recovery_page import PasswordRecoveryPage
from src.pages.header_page import HeaderPage
from src.pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Кликаем по кнопке "Восстановить пароль" на странице авторизации, сверяем текущий url с ожидаемым')
    def test_click_to_password_recovery_button_open_password_recovery_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_to_personal_account_button()
        login_page = LoginPage(driver)
        login_page.click_to_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)

        assert password_recovery_page.check_current_url(), "Урл не соответствует ожидаемому значению"

    @allure.title('Проверка перехода на страницу сброса пароля по кнопке «Восстановить»')
    @allure.description('На странице "Восстановление пароля" заполняем поле Email, кликаем по кнопке "Восстановить", '
                        'сверяем текущий url с ожидаемым')
    def test_click_to_recovery_button_open_reset_password_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open()
        email = user_registration_data()["email"]
        password_recovery_page.fill_email_field(email)
        password_recovery_page.click_to_recovery_button()
        reset_password_page = ResetPasswordPage(driver)

        assert reset_password_page.check_current_url(), "Урл не соответствует ожидаемому значению"

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('На странице "Сброс пароля" кликаем по кнопке "показать/скрыть пароль", проверяем, что поле активно')
    def test_click_to_show_password_button_make_password_field_active(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open()
        email = user_registration_data()["email"]
        password_recovery_page.fill_email_field(email)
        password_recovery_page.click_to_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.check_show_password_button_is_clickable()
        reset_password_page.click_to_show_password_button()

        assert reset_password_page.check_password_field_is_active(), "Поле не активно"