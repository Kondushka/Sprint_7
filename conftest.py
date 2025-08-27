import pytest
import requests
from data.urls import Urls
from data.helpers import RandomData as R

@pytest.fixture
def courier_data():
    return {
        "login": R.generate_random_string(5),
        "password": R.generate_random_string(9),
        "firstName": R.generate_random_string(4),
    }

@pytest.fixture
def courier_create():
    courier_data = {
        "login": R.generate_random_string(5),
        "password": R.generate_random_string(9),
        "firstName": R.generate_random_string(4),
    }

    requests.post(Urls.CREATE_COURIER_URL, json = courier_data)

    yield courier_data 
    login_response = requests.post(Urls.LOGIN_COURIER_URL, json={"login": courier_data["login"], "password": courier_data["password"]})
    id_courier = login_response.json()['id']
    requests.delete(f"{Urls.ID_COURIER_URL}{id_courier}")




@pytest.fixture
def order():
    order_data = {
        "firstName": R.generate_random_string(6),
        "lastName": R.generate_random_string(6),
        "address": R.generate_random_string(4),
        "metroStation": R.generate_random_number(),
        "phone": R.generate_random_phone(),
        "rentTime": R.generate_random_number(),
        "comment": R.generate_random_string(13)
        }

    track_order = {"track": None}
    
    yield order_data, track_order

    del_track = requests.put(Urls.CANCEL_ORDER_URL, params = track_order)

    assert del_track.status_code == 200, f'Заказ {track_order["track"]} нифига не удалился'
