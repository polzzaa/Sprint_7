import pytest
from helpers import delete_courier, create_courier, generate_data_for_new_courier
from data import ResponseText
import allure


class TestCreateCourier:


    @allure.title('Успешное создание курьера')
    def test_create_courier(self, generate_data_for_new_courier):
        response = create_courier(generate_data_for_new_courier)
        assert (response.status_code == 201 and response.text == ResponseText.create_courier_success)
        delete_courier(generate_data_for_new_courier)



    @allure.title('Тест на создание двух одинаковых курьеров')
    def test_create_two_identical_couriers(self, generate_data_for_new_courier):
        create_courier(generate_data_for_new_courier)
        response = create_courier(generate_data_for_new_courier)
        assert (response.status_code == 409 and response.json()['message'] == ResponseText.
                create_already_exist)

    @allure.title('Тест на создание курьера без пароля или логина')
    @pytest.mark.parametrize('login, password', [['',  generate_data_for_new_courier()['password']], [generate_data_for_new_courier()['login'], '']])
    def test_create_courier_without_data(self, generate_data_for_new_courier, login, password):
        response = create_courier(payload={
            "login": login,
            "password": password
        })
        assert (response.status_code == 400 and (response.json())['message'] == ResponseText.
                create_no_data)









