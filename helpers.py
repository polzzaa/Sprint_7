import allure
import requests
import random
import string
from urls import MAIN_URL, LOGIN_COURIER, CREATE_COURIER


@allure.title('Генерирование данных для курьера')
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


@allure.title('Удаление курьера')
def delete_courier(payload):
    response = requests.post(MAIN_URL + LOGIN_COURIER, data=payload)
    id_courier = response.json()["id"]
    requests.delete(f'{MAIN_URL}{CREATE_COURIER}/{id_courier}')


@allure.title('Создание курьера')
def create_courier(payload):
    return requests.post(MAIN_URL + CREATE_COURIER, data=payload)

def sigh_in_courier(payload):
    return requests.post(MAIN_URL + LOGIN_COURIER, data=payload)