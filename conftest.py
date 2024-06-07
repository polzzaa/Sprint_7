import allure
import requests
import random
import string
import pytest
from urls import MAIN_URL, CREATE_COURIER

@allure.title('Генерирование данных для курьера')
@pytest.fixture
def generate_data_for_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


@allure.title('Создание курьера')
@pytest.fixture
def create_courier(generate_data_for_new_courier):
    return requests.post(MAIN_URL + CREATE_COURIER, data=generate_data_for_new_courier)