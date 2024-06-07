import pytest
from helpers import delete_courier, sigh_in_courier, generate_data_for_new_courier
from data import ResponseText
import allure

class TestLoginCourier:


    @allure.title('Успешная авторизация курьера')
    def test_login_courier(self, generate_data_for_new_courier, create_courier):
        response = sigh_in_courier(generate_data_for_new_courier)
        assert response.status_code == 200 and type(response.json()['id']) == int
        delete_courier(generate_data_for_new_courier)


    @allure.title('Тест на авторизацию курьера без логина или пароля')
    @pytest.mark.parametrize('login, password', [['', generate_data_for_new_courier()['password']], [generate_data_for_new_courier()['login'], '']])
    def test_login_courier_without_data(self, create_courier, login, password):
        response = sigh_in_courier(payload={
            "login": login,
            "password": password
        })
        assert response.status_code == 400 and response.json()['message'] == ResponseText.login_no_data


    @allure.title('Тест на авторизацию курьера с неправильным логином или паролем')
    @pytest.mark.parametrize('login, password', [['123', generate_data_for_new_courier()['password']], [generate_data_for_new_courier()['login'], '123']])
    def test_login_courier_with_invalid_data(self, create_courier, login, password):
        response = sigh_in_courier(payload={
            "login": login,
            "password": password
        })
        assert response.status_code == 404 and response.json()['message'] == ResponseText.login_no_such_user








