import allure
import requests
from data.urls import Urls


class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, courier):
        courier_data = {
        "login": courier["login"],
        "password": courier["password"] }  

        with allure.step('Создаем курьера'):
            response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
            assert response.status_code == 201
            assert response.json() == {'ok': True}

        with allure.step('Логинимся'):
            response = requests.post(Urls.LOGIN_COURIER_URL, json=courier_data)
            assert response.status_code == 200
            assert "id" in response.json()

    @allure.title("Ошибка при неверном логине")
    def test_login_wrong_login(self, courier):
        courier_data = {
        "login": courier["login"] + 'new',
        "password": courier["password"] } 

        response = requests.post(Urls.LOGIN_COURIER_URL, json=courier_data)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при неверном пароле")
    def test_login_wrong_password(self, courier):
        courier_data = {
        "login": courier["login"],
        "password": courier["password"] + 'new' } 

        response = requests.post(Urls.LOGIN_COURIER_URL, json=courier_data)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при отсутствии логина")
    def test_login_no_login(self, courier):

        courier_data = {
        "login": None,
        "password": courier["password"] 
        }
        response = requests.post(Urls.LOGIN_COURIER_URL, json=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при отсутствии пароля")
    def test_login_no_password(self, courier):
        
        courier_data = {
        "login": courier["login"],
        "password": None }

        response = requests.post(Urls.LOGIN_COURIER_URL, json=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"