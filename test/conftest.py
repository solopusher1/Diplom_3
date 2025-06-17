import allure
from selenium import webdriver
from urls import PageUrls
from api.api_methods import ApiMethods
from helpers import *
import pytest

@pytest.fixture(params=['firefox', 'chrome'], autouse=True) # Запуск  Firefox и Chrome
def driver(request):
    driver = None
    with allure.step(f'Запуск браузера {request.param}'):
        if request.param == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(PageUrls.HOME_PAGE)
        elif request.param == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(PageUrls.HOME_PAGE)

    yield driver
    with allure.step(f'Закрытие браузера {request.param}'):
        driver.quit()

@pytest.fixture() # Рега нового пользователя и его удаление после завершения теста
def user():
    reg_values = user_registration_data()
    user_create_response = ApiMethods.create_user(reg_values)
    email = reg_values["email"]
    password = reg_values["password"]
    yield email, password
    token = user_create_response.json()["accessToken"]
    ApiMethods.delete_user(token)