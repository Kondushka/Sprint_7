import allure
import requests
from data.urls import Urls


@allure.title("Создание нового курьера cо всеми данными")

def test_create_courier(courier):

    with allure.step('Создаем курьера'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    login_data = {
        "login": courier["login"],
        "password": courier["password"] }
    
    with allure.step('Логинимся и удаляем курьера'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        id_courier = response.json()['id']
        del_courier = requests.delete(f'{Urls.ID_COURIER_URL}{id_courier}')
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {'ok': True}

@allure.title("Создание курьера — без не обязательного поля firstName")
def test_create_courier_no_firstName(courier):
    
    login_data = {
        "login": courier["login"],
        "password": courier["password"]
    }

    with allure.step('Создаем курьера без поля firstName'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = login_data)
    
        assert response.status_code == 201
        assert response.json() == {'ok': True}
    
    with allure.step('Логинимся и удаляем курьера'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        id_courier = response.json()['id']
        del_courier = requests.delete(f'{Urls.ID_COURIER_URL}{id_courier}')
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {'ok': True}

