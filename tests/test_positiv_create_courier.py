import allure
import requests
from data.urls import Urls


@allure.suite("Создание курьера / Позитивный сценарий")

class TestPositivCreateCourier:

    @allure.title("Создание нового курьера со всеми данными")
    def test_courier_create(self, courier_data):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        login_response = requests.post(Urls.LOGIN_COURIER_URL, json={"login": courier_data["login"], "password": courier_data["password"]})
        id_courier = login_response.json()['id']
        requests.delete(f"{Urls.ID_COURIER_URL}{id_courier}")        

    @allure.title("Создание курьера без необязательного поля firstName")
    def test_courier_create_no_firstName(self, courier_data):

        response = requests.post(Urls.CREATE_COURIER_URL, json = {"login": courier_data["login"], "password": courier_data["password"]})        
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        login_response = requests.post(Urls.LOGIN_COURIER_URL, json={"login": courier_data["login"], "password": courier_data["password"]})
        id_courier = login_response.json()['id']
        requests.delete(f"{Urls.ID_COURIER_URL}{id_courier}")
        

