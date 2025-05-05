import re
from typing import Any

from src.masks import get_mask_account, get_mask_card_number


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


def get_date(date: str) -> str:
    """
    Функция меняющая формат даты.
    """

    date_1 = date[:10].replace("-", "")
    day = date_1[6:8]
    month = date_1[4:6]
    year = date_1[:4]
    if not re.match(r"^\d{4}-\d{2}-\d{2}T", date):
        raise ValueError("Неправильно введены данные!")
    elif len(date) != 26 and date_1.isdigit():
        raise ValueError("Неправильная длина данных!")
    elif int(day) > 31 or day == "00":
        raise ValueError("Неправильно введена дата!")
    elif int(month) > 12 or month == "00":
        raise ValueError("Месяц указан неверно")
    elif int(year) > 9000 or year == "0000":
        raise ValueError("Год указан неверно")
    elif int(day) > 29 and month == "02":
        raise ValueError("Неправильно введена дата!")
    else:
        day_month_year = day + "." + month + "." + year
    return day_month_year


if __name__ == "__main__":
    number = input("Введите номер карты или номер счета: ")
    print(mask_account_card(number))
    date = input("Введите дату: ")
    print(get_date(date))
