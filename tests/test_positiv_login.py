import allure
import requests
from data.urls import Urls


@allure.title("Успешный вход в систему")

def test_positiv_login(courier):

    with allure.step('Создаем курьера'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    login_data = {
        "login": courier["login"],
        "password": courier["password"] }
    
    with allure.step('Логинимся c корректными данными'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        
        assert response.status_code == 200
        assert 'id' in response.json()

    with allure.step('Удаляем курьера'):
        id_courier = response.json()['id']
        del_courier = requests.delete(f"{Urls.ID_COURIER_URL}{id_courier}")
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {'ok': True}

