import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_1(dictionaries_1: list) -> None:
    result = list(filter_by_currency(dictionaries_1, "USD"))
    expected = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
         'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
         'to': 'Visa Platinum 8990922113665229'}
    ]
    assert result == expected


def test_filter_by_currency_2(dictionaries_1: list) -> None:
    result = list(filter_by_currency(dictionaries_1, "RUB"))
    expected = [
        {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
         'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
         'to': 'Счет 74489636417521191160'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
         'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
         'to': 'Счет 14211924144426031657'}
    ]
    assert result == expected


def test_filter_by_currency_3() -> None:
    with pytest.raises(TypeError):
        filter_by_currency()


@pytest.mark.parametrize("dictionaries, currency, expected", [
    (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации", "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
                 "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
                 "to": "Счет 14211924144426031657"}
            ],
            "USD",
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации", "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
            ]
    ),
    (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации", "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
                 "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
                 "to": "Счет 14211924144426031657"}
            ],
            "",
            []
    ),
    (
            [],
            "USD",
            []
    ),
    (
            [],
            "",
            []
    ),
])
def test_filter_by_currency_4(dictionaries: list, currency: str, expected: str) -> None:
    result = list(filter_by_currency(dictionaries, currency))
    assert result == expected


def test_transaction_descriptions(dictionaries_1):
    result = list(transaction_descriptions(dictionaries_1))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert result == expected


@pytest.mark.parametrize("dictionaries, expected", [
    (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации", "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
                 "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
                 "to": "Счет 14211924144426031657"}
            ], ["Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации"]
    ),
    (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "from": "Счет 44812258784861134719",
                 "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "from": "Visa Platinum 1246377376343588",
                 "to": "Счет 14211924144426031657"}
            ],
            ['Отсутствует описание',
             'Отсутствует описание',
             'Отсутствует описание',
             'Отсутствует описание',
             'Отсутствует описание']

    ),
    (
            [],
            []
    ),
    (
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
              "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
              "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"},
             {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
              "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"},
             {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
              "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
              "from": "Счет 44812258784861134719",
              "to": "Счет 74489636417521191160"},
             {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
              "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
              "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
              "to": "Visa Platinum 8990922113665229"},
             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
              "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
              "from": "Visa Platinum 1246377376343588",
              "to": "Счет 14211924144426031657"}],
            ['Отсутствует описание',
             'Перевод со счета на счет',
             'Отсутствует описание',
             'Перевод с карты на карту',
             'Отсутствует описание']
    ),
])
def test_transaction_descriptions(dictionaries, expected):
    result = list(transaction_descriptions(dictionaries))
    assert result == expected

def test_card_number_generator_1():
    generator = card_number_generator(1,5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"

def test_card_number_generator_2():
    generator = card_number_generator(9999999999999990,10000000000000000)
    assert next(generator) == "9999 9999 9999 9990"
    assert next(generator) == "9999 9999 9999 9991"
    assert next(generator) == "9999 9999 9999 9992"
    assert next(generator) == "9999 9999 9999 9993"
    assert next(generator) == "9999 9999 9999 9994"
    assert next(generator) == "9999 9999 9999 9995"
    assert next(generator) == "9999 9999 9999 9996"
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"
