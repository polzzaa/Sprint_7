import pytest
from helpers import *
from data import ResponseText
import allure


class TestCreateCourier:
    payload = generate_data_for_new_courier()

    @allure.title('Успешное создание курьера')
    def test_create_courier(self):
        response = create_courier(self.payload)
        assert (response.status_code == 201 and response.text == ResponseText.create_courier_success)
        delete_courier(self.payload)



    @allure.title('Тест на создание двух одинаковых курьеров')
    def test_create_two_identical_couriers(self):
        create_courier(self.payload)
        response = create_courier(self.payload)
        assert (response.status_code == 409 and response.json()['message'] == ResponseText.
                create_already_exist)

    @allure.title('Тест на создание курьера без пароля или логина')
    @pytest.mark.parametrize('login, password', [['', payload['password']], [payload['login'], '']])
    def test_create_courier_witout_data(self, login, password):
        response = create_courier(payload={
            "login": login,
            "password": password
        })
        assert (response.status_code == 400 and (response.json())['message'] == ResponseText.
                create_no_data)









