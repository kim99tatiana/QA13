# Ким Татьяна, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import order
import data


def test_status_of_order_is_200():
    response_order = order.post_new_order(data.order_body_full)  # 1 шаг - запрос на создание заказа
    track = {"t": response_order.json()["track"]}  # 2 шаг - сохраняем номер трека заказа
    response = order.getting_order_data(track)
    assert response.status_code == 200  # Проверяем, равен ли код ответа 200
