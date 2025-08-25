import allure
import pytest
import requests
from data.urls import Urls




@allure.title("Создание курьера — без обязательного поля (login/password)")
@pytest.mark.parametrize("missing_key", ["password", "login"])

def test_create_courier_no_data(courier, missing_key):
    with allure.step(f'Ловим ошибку при создании курьера без обязательного поля {missing_key}'):
        courier.pop(missing_key)
        
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
        
        assert response.status_code == 400
        assert response.json()["message"]  == "Недостаточно данных для создания учетной записи"




@allure.title("Дублирование курьера")

def test_create_doble_courier(courier):

    with allure.step('Создаем нового курьера'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    with allure.step('Ловим ошибку при создании курьера с теми же данными (полный дубль)'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    login_data = {
        "login": courier["login"],
        "password": courier["password"] }
    
    with allure.step('Логинимся и удаляем курьера'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        id_courier = response.json()['id']
        del_courier = requests.delete(f'{Urls.ID_COURIER_URL}{id_courier}')
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {"ok": True}


@allure.title("Создание курьера с уже существующим логином")

def test_create_doble_courier(courier):
    with allure.step('Создаем нового курьера'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
        assert response.status_code == 201
        assert response.json() == {"ok": True}


    clone_login_courier = {
        "login": courier["login"],
        "password": courier["password"] + "_new",
        "firstName": courier["firstName"] + "_new",
    }
    with allure.step('Ловим ошибку при создании курьера с таким же логином'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = clone_login_courier)
    
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    login_data = {
        "login": courier["login"],
        "password": courier["password"] }
    
    with allure.step('Логинимся и удаляем курьера'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        id_courier = response.json()['id']
        del_courier = requests.delete(f'{Urls.ID_COURIER_URL}{id_courier}')
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {"ok": True}

