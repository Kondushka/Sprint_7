import allure
import pytest
import requests
from data.urls import Urls
from data.helpers import TextResponse as TR



@allure.suite("Создание курьера / Негативный сценарий")
class TestNegativCreateCourier:

    @allure.title("Создание курьера — без обязательного поля")
    @pytest.mark.parametrize("missing_key", ["password", "login"])
    def test_create_courier_no_data(self, courier_create, missing_key):

        with allure.step(f'Ловим ошибку при создании курьера без обязательного поля {missing_key}'):
            creds = {"login": courier_create["login"], "password": courier_create["password"]}
            creds.pop(missing_key)
            response = requests.post(Urls.CREATE_COURIER_URL, json = creds)            
            assert response.status_code == 400
            assert response.json()["message"]  == TR.MISSING_FIELDS




    @allure.title("Дублирование курьера")
    def test_create_doble_courier(self, courier_create):

        with allure.step('Ловим ошибку при создании курьера с теми же данными (полный дубль)'):
            response = requests.post(Urls.CREATE_COURIER_URL, json = courier_create)
            assert response.status_code == 409
            assert response.json()["message"] == TR.DUPLICATE_LOGIN

    

    @allure.title("Создание курьера с уже существующим логином")

    def test_create_same_login(self, courier_create):

        wrong_courier_create = {
            "login": courier_create["login"],
            "password": courier_create["password"] + "_new",
            "firstName": courier_create["firstName"] + "_new"}
        with allure.step('Ловим ошибку при создании курьера с таким же логином'):
            response = requests.post(Urls.CREATE_COURIER_URL, json = wrong_courier_create)
            assert response.status_code == 409
            assert response.json()["message"] == TR.DUPLICATE_LOGIN


