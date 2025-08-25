import allure
import requests
from data.urls import Urls



@allure.title("Получение списка заказов")

def test_get_order_list():
    response = requests.get(Urls.ORDER_URL)
    order_list = response.json()
    assert response.status_code == 200
    assert "orders" in order_list