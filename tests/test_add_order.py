import allure
import pytest
import requests
from data.urls import Urls


@allure.title("Создание заказа — варианты цвета: один / оба / без цвета")
@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])

def test_add_order(courier, order, color):

    with allure.step('Создаем курьера'):
        create_response = requests.post(Urls.CREATE_COURIER_URL, json = courier)
    
        assert create_response.status_code == 201
        assert create_response.json() == {'ok': True}

    login_data = {
        "login": courier["login"],
        "password": courier["password"] }
    
    with allure.step('Логинимся c корректными данными'):
        login_response = requests.post(Urls.LOGIN_COURIER_URL, json = login_data)
        assert login_response.status_code == 200
        assert 'id' in login_response.json()


    with allure.step(f"Создаем заказ с цветом {color}"):

        if color is None:
            order.pop("color", None)
        else:
            order["color"] = color


        order_response = requests.post(Urls.ORDER_URL, json = order)
        track_order = order_response.json()["track"]

        assert order_response.status_code == 201
        assert 'track' in order_response.json()

    with allure.step('Отменяем заказ'):
        order_cancel = requests.put(Urls.CANCEL_ORDER_URL, params={"track": track_order})
        assert order_cancel.status_code == 200
        assert order_cancel.json() == {'ok': True}

    with allure.step('Удаляем курьера'):
        id_courier = login_response.json()['id']
        del_courier = requests.delete(f"{Urls.ID_COURIER_URL}{id_courier}")
        
        assert del_courier.status_code  == 200
        assert del_courier.json() == {'ok': True}

