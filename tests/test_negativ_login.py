import allure
import requests
import pytest
from data.urls import Urls


@allure.title("Вход в систему без обязательного поля (login/password)")
@pytest.mark.parametrize("missing_key", ["login", "password"])

def test_login_no_data(courier, missing_key):

    login_data = {"login": courier["login"], "password": courier["password"]}
    login_data.pop(missing_key)

    with allure.step(f'Ловим ошибку при попытке залогиниться без обязательного поля {missing_key}'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        
        if response.status_code == 504:
            pytest.skip(f"Стенд нестабилен: {response.status_code} {response.text}")
            
        assert response.status_code == 400
        assert response.json()["message"]  == "Недостаточно данных для входа"

    

@allure.title("Вход в систему с некорректными данными (login/password)")
@pytest.mark.parametrize('wrong_data', ["login", "password"])


def test_login_wrong_data(courier, wrong_data):

    with allure.step('Создаем курьера'):
        response = requests.post(Urls.CREATE_COURIER_URL, json = courier)   
        
        assert response.status_code == 201
        assert response.json() == {'ok': True}
    
    if wrong_data == "password":
        wrong_login_data = {"login": courier["login"], "password": "Pass12345"}

    if wrong_data == "login":
        wrong_login_data = {"login": "qwerty", "password": courier["password"]}

    with allure.step(f'Ловим ошибку при попытке залогиниться с некорректными данными {wrong_data}'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = wrong_login_data)

        if response.status_code >= 500:
            pytest.skip(f"Стенд нестабилен: {response.status_code} {response.text}")
        
        assert response.status_code == 404 
        assert response.json()["message"] == "Учетная запись не найдена"

    
    with allure.step('Логинимся и удаляем курьера'):
        response = requests.post(Urls.LOGIN_COURIER_URL, json = courier)
        id_courier = response.json()['id']
        del_courier = requests.delete(f"{Urls.ID_COURIER_URL}{id_courier}")
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {"ok": True}  

