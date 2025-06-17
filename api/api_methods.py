import allure
import requests
from urls import ApiUrls

class ApiMethods:
    @staticmethod
    @allure.step('Создание нового пользователя через API ручку')
    def create_user(data):
        response = requests.post(ApiUrls.USER_CREATION, data=data)

        return response

    @staticmethod
    @allure.step('Удаление пользователя через API ручку')
    def delete_user(token):
        requests.delete(ApiUrls.DELETE_USER + token)