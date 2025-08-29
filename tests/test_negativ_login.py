import allure
import requests
import pytest
from data.urls import Urls
from data.data import TextResponse as TR

@allure.suite("Вход в систему / Негативный сценарий")
class TestNegativLogin:

    @allure.title("Вход в систему без логина")
    def test_no_login(self, courier_create):

        with allure.step(f'Ловим ошибку при попытке залогиниться без логина'):
            response = requests.post(Urls.LOGIN_COURIER_URL, json = {"password": courier_create["password"]})
            if response.status_code >= 500:
                pytest.skip(f"Стенд нестабилен: {response.status_code} {response.text}")    
            assert response.status_code == 400
            assert response.json()["message"]  == TR.LOGIN_DATA_MISSING



    @allure.title("Вход в систему без пароля")
    def test_no_password(self, courier_create):

        with allure.step(f'Ловим ошибку при попытке залогиниться без пароля'):
            response = requests.post(Urls.LOGIN_COURIER_URL, json = {"login": courier_create["login"]})
            if response.status_code >= 500:
                pytest.skip(f"Стенд нестабилен: {response.status_code} {response.text}")    
            assert response.status_code == 400
            assert response.json()["message"]  == TR.LOGIN_DATA_MISSING
        

    @allure.title("Вход в систему с некорректным паролем")
    def test_password_wrong(self, courier_create):

        with allure.step(f'Ловим ошибку при попытке залогиниться с некорректным паролем'):
            login_response = requests.post(Urls.LOGIN_COURIER_URL, json = {"login": courier_create["login"], "password": "Pass12345"})
            if login_response.status_code >= 500:
                pytest.skip(f"Стенд нестабилен: {login_response.status_code} {login_response.text}") 
            assert login_response.status_code == 404 
            assert login_response.json()["message"] == TR.USER_NOT_FOUND


    @allure.title("Вход в систему с некорректным логином")
    def test_login_wrong(self, courier_create):

        wrong_login_data = {"login": "qwerty", "password": courier_create["password"]}
        with allure.step(f'Ловим ошибку при попытке залогиниться с некорректным логином'):
            login_response = requests.post(Urls.LOGIN_COURIER_URL, json = wrong_login_data)
            if login_response.status_code >= 500:
                pytest.skip(f"Стенд нестабилен: {login_response.status_code} {login_response.text}")
            assert login_response.status_code == 404 
            assert login_response.json()["message"] == TR.USER_NOT_FOUND
