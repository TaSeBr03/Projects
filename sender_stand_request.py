#  Татьяна Бронман, 21-я когорта Финальный проект. Инженер по тестированию плюс
import requests
from configuration import url_create, url_get
def create_order(order_data):
    response_create = requests.post(url_create, json=order_data)
    return response_create
def get_order(track):
    url = url_get + str(track)
    response_get = requests.get(url)
    return response_get