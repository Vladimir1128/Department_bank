# Проект "Виджет личного кабинета."

Проект "Виджет личного кабинета."разрабатывается для клиентов банка, написан на Python. Виджет анализируют десятки параметров, чтобы максимально быстро и точно выдавать пользователю ровно то, что нужно ему.

## Пояснение:

Данный проект является бэкенд-разработкой.

## Работа модуля [masks.py](src/masks.py)

Первая функция создает маску в формате **XXXX XX** **** XXXX, где 
X
 — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками
```
def get_mask_card_number(number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    number_str = str(number)
    mask_number = number_str[:4] + " " + number_str[4:6] + ("*" * 2 + " " + "*" * 4) + " " + number_str[12:]
    return mask_number
```
Вторая функция в этом модуле создает маску в формате **XXXX
, где 
X
 — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. 

```
def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. """
    account_str = str(account)
    mask_account = ("*" * 2) + account_str[-4:]
    return mask_account
```

## Работа модуля [widget.py](src/widget.py)

Функция взаимодействует через импорт `from src.masks import get_mask_account, get_mask_card_number`
используя функции модуля [masks.py](src/masks.py).


В функцию подается название карты и ее номер или номер счета и выводится название и номер в маске
```
def mask_account_card(number: Any) -> str:
    """
    Функция обрабатывающая информацию о картах и о счетах
    """
    if "Maestro" in number and len(number) == 24:
        return "Maestro " + str(get_mask_card_number(number[8:]))
    elif "MasterCard" in number and len(number) == 27:
        return "MasterCard " + str(get_mask_card_number(number[11:]))
    elif "Visa Classic" in number and len(number) == 29:
        return "Visa Classic " + str(get_mask_card_number(number[13:]))
    elif "Visa Platinum " in number and len(number) == 30:
        return "Visa Platinum " + str(get_mask_card_number(number[14:]))
    elif "Visa Gold" in number and len(number) == 26:
        return "Visa Gold " + str(get_mask_card_number(number[10:]))
    elif "Счет" in number and len(number) == 25:
        return "Счет " + str(get_mask_account(number[5:]))
    else:
        return "Неправильно введены данные!"
```

Вторая функция в этом модуле принимает на вход строку с датой в формате 
"2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате 
"ДД.ММ.ГГГГ"
 (
"11.03.2024"
).

```
def get_date(date: str) -> str:
    """
    Функция меняющая формат даты.
    """
    date_1 = date[:10].replace("-", " ").split()
    day_month_year = date_1[2] + "." + date_1[1] + "." + date_1[0]
    return day_month_year
```


## Работа модуля [processing.py](src/processing.py)
Первая функция принимает список словарей и опционально значение для ключа 
state
 (по умолчанию 
'EXECUTED'
). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state
 соответствует указанному значению.
```
def filter_by_state(list_dictionaries: list, state: str) -> list:
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
```


Вторая функция в этом модуле принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
date
).

```
def sort_by_date(list_dictionaries: list, reverse: bool = True) -> list:
    """
    Функция сортировки словарей по 'date'.
    """
    sorted_dates = sorted(list_dictionaries, key=lambda date: date["date"], reverse=reverse)
    return sorted_dates
```

## *Тестирование:*

В пакете tests созданы модули: 
         
[test_masks.py](tests/test_masks.py),
```
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_correct_number(correct_number):
    assert get_mask_card_number(7000792289606361) == correct_number
```
[test_widget.py](tests/test_widget.py),
```
import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('number, expected', [("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                                              ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                              ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                              ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                              ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                              ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card_correct(number, expected):
    assert mask_account_card(number) == expected
```

[test_processing.py](tests/test_processing.py),
```
import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import variable_1


@pytest.mark.parametrize("state, expected",
                         [("EXECUTED", [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                        {"id": 939719570, "state": "EXECUTED",
                                         "date": "2018-06-30T02:08:58.425572"}, ]),
                          ("CANCELED", [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                        {"id": 615064591, "state": "CANCELED",
                                         "date": "2018-10-14T08:21:33.419441"}, ])])
def test_filter_by_state_by_default_1(state, variable_1, expected):
    assert filter_by_state(variable_1, state) == expected
```

[conftest.py](tests/conftest.py)
```

@pytest.fixture
def variable_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
```
### Установка библиотеке pytest-cov :
Следующей командой: 
```
poetry add --group dev pytest-cov
```

Для тестирования кода в Pycharm используется команда ```pytest```
Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:

```poetry run pytest --cov```,

```pytest --cov```,

```poetry run pytest --cov```

Чтобы сгенерировать отчет о покрытии в HTML-формате:```pytest --cov=src --cov-report=html```

### Генераторы
Генераторы позволяют генерировать элементы последовательности без хранения их всех в памяти; работать с большими объемами данных; снижать использование памяти и ускорять выполнение программы.

[test_generators.py](tests/test_generators.py)

```
def test_filter_by_currency_1(dictionaries_1: list) -> None:
    result = list(filter_by_currency(dictionaries_1, "USD"))
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    assert result == expected
```

### Декораторы
Это - это функция, которая принимает другую функцию в качестве аргумента и изменяет ее поведение без изменения самой функции.
```
def log(filename: Any = None) -> Any:
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any,
                    **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: Any,
                y: Any) -> Any:
    return x + y


my_function(1, 2)
```
### Установка библиотеке pandas :
Следующей командой: 
```
poetry add pandas
```
## Работа модуля [data_frame.py](src/data_frame.py)
Эта функция работает с данными в формате .csv

```
def my_csv(data_csv: Any) -> str | None:
    """
    Function reads .csv
    """
    try:
        csv_data = pd.read_csv(data_csv, sep=";")
        print(csv_data.shape)
        head_csv = csv_data.head()
        js_dict = head_csv.to_dict(orient="records")
        return json.dumps(js_dict, ensure_ascii=False, indent=4)

    except FileNotFoundError as file:
        print(f"File {file} not found")
    return None
```
Эта функция работает с данными в формате .excel
```
def my_excel(data_excel: Any) -> str | None:
    """
    Function reads .excel
    """
    try:
        excel_data = pd.read_excel(data_excel)
        print(excel_data.shape)
        head_excel = excel_data.head()
        js_dict = head_excel.to_dict(orient="records")
        return json.dumps(js_dict, ensure_ascii=False, indent=4)

    except FileNotFoundError as file:
        print(f"File {file} not found")
    return None
```

## Лицензия:


Этот проект лицензирован по [лицензии MIT](LICENSE).
