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

## Лицензия:


Этот проект лицензирован по [лицензии MIT](LICENSE).
