import allure
import requests
from data.urls import Urls



@allure.suite("Получение списка заказов")
class TestOrderLust:
    def test_get_order_list(self):
        response = requests.get(Urls.ORDER_URL)
        order_list = response.json()
        assert response.status_code == 200
        assert "orders" in order_list