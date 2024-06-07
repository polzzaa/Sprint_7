import requests
import allure
from urls import MAIN_URL, ORDER_LIST


class TestGetOrderList:

    @allure.title('Успешное получение списка заказов')
    def test_get_order_list(self):
        response = requests.get(MAIN_URL + ORDER_LIST)
        assert response.status_code == 200 and 'track' in response.text

