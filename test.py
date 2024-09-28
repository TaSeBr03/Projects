#  Татьяна Бронман, 21-я когорта Финальный проект. Инженер по тестированию плюс
from data import order_data
from sender_stand_request import create_order, get_order
def test_order_creation_and_retrieval():
    response_create = create_order(order_data)
    order_track = response_create.json()["track"]
    response_get = get_order(order_track)
    assert response_get.status_code == 200