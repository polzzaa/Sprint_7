class OrderData:
    data = {
        'firstname': "Иван",
        'lastname': 'Иванов',
        'address': 'г. Москва',
        'metroStation': 1,
        'phone': '+7 999 999 99 99',
        'rentTime': 1,
        'deliveryDate': '2024-06-10',
        'comment': 'Тест',
        'color' : ['BLACK']
    }

class ResponseText:
    create_courier_success = '{"ok":true}'
    create_no_data = "Недостаточно данных для создания учетной записи"
    create_already_exist = "Этот логин уже используется. Попробуйте другой."
    login_no_data = "Недостаточно данных для входа"
    login_no_such_user = "Учетная запись не найдена"