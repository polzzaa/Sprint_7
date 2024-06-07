import allure
import pytest
import json
import requests
from data import OrderData
from urls import CREATE_ORDER, MAIN_URL

class TestCreateOrder:

    @allure.title('Тест на создание заказа с разными вариантами цветов')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"],
                                       ["BLACK", "GRAY"], [""]])
    def test_create_order_different_color(self, color):
        OrderData.data['color'] = [color]
        response = requests.post(MAIN_URL + CREATE_ORDER, data=json.dumps(OrderData.data))
        assert response.status_code == 201 and type((response.json())['track']) == int
