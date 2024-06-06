import pytest
from helpers import *
from data import ResponseText
import allure

class TestLoginCourier:
    payload = generate_data_for_new_courier()
    create_courier(payload)

    @allure.title('Успешная авторизация курьера')
    def test_login_courier(self):
        response = sigh_in_courier(self.payload)
        assert response.status_code == 200 and type(response.json()['id']) == int
        delete_courier(self.payload)


    @allure.title('Тест на авторизацию курьера без логина или пароля')
    @pytest.mark.parametrize('login, password', [['', payload['password']], [payload['login'], '']])
    def test_login_courier_witout_data(self, login, password):
        response = sigh_in_courier(payload={
            "login": login,
            "password": password
        })
        assert response.status_code == 400 and response.json()['message'] == ResponseText.login_no_data


    @allure.title('Тест на авторизацию курьера с неправильным логином или паролем')
    @pytest.mark.parametrize('login, password', [['123', payload['password']], [payload['login'], '123']])
    def test_login_courier_with_invalid_data(self, login, password):
        response = sigh_in_courier(payload={
            "login": login,
            "password": password
        })
        assert response.status_code == 404 and response.json()['message'] == ResponseText.login_no_such_user








