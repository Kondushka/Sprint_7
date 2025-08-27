import allure
import requests
from data.urls import Urls


@allure.suite("Создание заказа")

class TestOtrder:

    @allure.title("Создание заказа — цвет: GREY")
    def test_add_order_grey(self, order):

        order_data, track_order = order
        grey_order = {**order_data, "color": ["GREY"]}
        order_response = requests.post(Urls.ORDER_URL, json = grey_order)
        assert order_response.status_code == 201
        assert 'track' in order_response.json()
        track_order["track"] = order_response.json()["track"]



    @allure.title("Создание заказа — цвет: BLACK")
    def test_add_order_black(self, order):

        order_data, track_order = order
        gblack_order = {**order_data, "color": ["BLACK"]}
        order_response = requests.post(Urls.ORDER_URL, json = gblack_order)
        assert order_response.status_code == 201
        assert 'track' in order_response.json()
        track_order["track"] = order_response.json()["track"]


    @allure.title("Создание заказа — цвета: GREY and BLACK")
    def test_add_order_grey_and_black(self, order):

        order_data, track_order = order
        both_colors = {**order_data, "color": ["GREY", "BLACK"]}
        order_response = requests.post(Urls.ORDER_URL, json = both_colors)
        assert order_response.status_code == 201
        assert 'track' in order_response.json()        
        track_order["track"] = order_response.json()["track"]


    @allure.title("Создание заказа без цвета")
    def test_add_order_no_color(self, order):

        order_data, track_order = order
        order_response = requests.post(Urls.ORDER_URL, json = order_data)

        assert order_response.status_code == 201
        assert 'track' in order_response.json()      
        track_order["track"] = order_response.json()["track"]