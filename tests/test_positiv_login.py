import allure
import requests
from data.urls import Urls

@allure.suite("Вход в систему / Позитивный сценарий")
class TestPositivLogin:
    def test_positiv_login(self, courier_create):
        response = requests.post(Urls.LOGIN_COURIER_URL, json={
        "login": courier_create["login"],
        "password": courier_create["password"]})
        assert response.status_code == 200
        assert 'id' in response.json()
        
