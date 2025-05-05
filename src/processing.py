from typing import Any

from src.widget import get_date


def filter_by_state(list_dictionaries: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    list_dictionaries_1 = []
    for key in list_dictionaries:
        if state == key["state"]:
            list_dictionaries_1.append(key)
        elif state == "" and key["state"] == "EXECUTED":
            list_dictionaries_1.append(key)
    return list_dictionaries_1


def sort_by_date(list_dictionaries: list, reverse: bool = True) -> list[Any] | None:
    """
    Функция сортировки словарей по 'date'.
    """
    for key in list_dictionaries:
        if get_date(key["date"]) == "Неправильно введены данные!":
            raise ValueError("Некорректно введена дата!")
        else:
            sorted_dates = sorted(list_dictionaries, key=lambda date: date["date"], reverse=reverse)
            return sorted_dates


if __name__ == "__main__":
    state = input("Введите состояние: ")
    list_dictionaries = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},

    ]
    result = filter_by_state(list_dictionaries, state)
    print(result)
    reverse = True
    print(sort_by_date(list_dictionaries, reverse))
