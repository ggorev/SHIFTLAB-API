import requests
import json


# Вход в систему
def sign_in(url="https://shiftlab.cft.ru:1337/api/sign-in"):
    payload = json.dumps({
        "name": "tester",
        "password": "SuperSecret123"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


jwt = sign_in().json().get("jwt")
refreshToken = sign_in().json().get("refreshToken")


# Обновление jwt и refresh токена
def token_refresh(url="https://shiftlab.cft.ru:1337/api/token-refresh"):
    global jwt
    global refreshToken
    payload = json.dumps({
        "refreshToken": f"{refreshToken}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jwt = response.json().get("jwt")
    refreshToken = response.json().get("refreshToken")
    return response


# Отправка решения по согласованию отпуска
def vacation_request_decision(url="https://shiftlab.cft.ru:1337/api/tasks/decision/vacation?name=inci"):
    global jwt
    payload = json.dumps({
        "id": 1,
        "status": "APPROVED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Получение списка заявок на согласование отпуска
def vacation_requests(url="https://shiftlab.cft.ru:1337/api/vacation/requests?name=inci"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список городов заданной страны для командировок
def businesstrip_country_cities(url="https://shiftlab.cft.ru:1337/api/business-trip/Россия/cities"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает архив командировок
def businesstrip_archive(url="https://shiftlab.cft.ru:1337/api/business-trip/archive"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список стран для командировок
def businesstrip_countries(url="https://shiftlab.cft.ru:1337/api/business-trip/countries"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Отправление заявки на командировку
def businesstrip_request(url="https://shiftlab.cft.ru:1337/api/business-trip/request"):
    global jwt
    payload = json.dumps({
        "additionalWishes": "ut",
        "bookHotel": False,
        "city": "nostrud amet sit proident",
        "country": "velit aliqua dolore",
        "employee": "Hideo Kojima",
        "firstDate": -90656952,
        "lastDate": -93218658,
        "returnTickets": True,
        "ticketsType": "TRAIN",
        "tripAim": "laborum ad voluptate Lorem quis"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Обработка заявки на отправку справки на почту (на данный момент является заглушкой)
def certificate_get_email(url="https://shiftlab.cft.ru:1337/api/certificate/get/email"):
    global jwt
    payload = json.dumps({
        "certificateDate": "20.02.2004",
        "certificateType": "elit pariatur enim sunt dolore",
        "destinationEmail": "Lorem@212.ru",
        "originalNecessary": True
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Инициирует скачивание документа на устройство пользователя
def certificate_load_url(url="https://shiftlab.cft.ru:1337/api/certificate/load/inci"):
    global jwt
    payload = {}
    headers = {
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Добавляет заявку на получение справки
def certificate_send(url="https://shiftlab.cft.ru:1337/api/certificate/send?name=inci"):
    global jwt
    payload = json.dumps({
        "certificateDate": "20.02.2004",
        "certificateType": "eu sint",
        "originalNecessary": True
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает cписок сотрудников компании для последующего их выбора в качестве заместителя на время отпуска
def vacation_alternates(url="https://shiftlab.cft.ru:1337/api/vacation/alternates?name=inci"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Получение краткой информации о всех существующих задачах
def inventory(url="https://shiftlab.cft.ru:1337/api/inventory"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Добавление задачи на инвентаризацию
def inventory_details(url="https://shiftlab.cft.ru:1337/api/inventory/details"):
    global jwt
    payload = json.dumps({
        "comment": "cupidatat est aliquip commodo",
        "date": -42083874,
        "listBarcode": [
            "aliqua laboris",
            "officia"
        ],
        "location": "laborum voluptate",
        "status": "PERFORMED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает список забронированных переговорных
def booked_booked_meeting_rooms(url="https://shiftlab.cft.ru:1337/api/booked/booked_meeting_rooms"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает имя пользователя
def profile_get_name(url="https://shiftlab.cft.ru:1337/api/profile/get-name"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Отправляет номер электронного больничного и период больничного
def sick_leave_request(url="https://shiftlab.cft.ru:1337/api/sick_leave/request"):
    global jwt
    payload = json.dumps({
        "sickLeaveNumber": "reprehenderit occaecat",
        "sickLeavePeriodFirst": -4796381,
        "sickLeavePeriodLast": 61455117
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает модель, которая содержит в себе список заданий
def tasks_feed(url="https://shiftlab.cft.ru:1337/api/tasks/feed?name=inci"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает количество дней отпуска на сегодняшний день, на конец года и дату последнего перерасчета отпускных дней
def vacation_days_info(url="https://shiftlab.cft.ru:1337/api/vacation/days_info"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список отпускных дней относительно дня недели, недели месяца и дня месяца для текущего пользователя
def vacation_periods_year_month(url="https://shiftlab.cft.ru:1337/api/vacation/periods/-1950555/-1950555"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список периодов отпусков для текущего пользователя
def vacation_vacations_list(url="https://shiftlab.cft.ru:1337/api/vacation/vacations_list"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список категорий товаров
def categories(url="https://shiftlab.cft.ru:1337/api/categories"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список товаров на складе
def warehouse(url="https://shiftlab.cft.ru:1337/api/warehouse"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список заявок на выдачу товаров со склада
def warehouse_requests_from_warehouse(
        url="https://shiftlab.cft.ru:1337/api/warehouse/requests_from_warehouse?name""=inci"):
    global jwt
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response
