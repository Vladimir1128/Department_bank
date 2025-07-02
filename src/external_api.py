import os
from typing import Any, Generator

import requests
from dotenv import load_dotenv

from .utils import way_to_json

json_file = "data/operations.json"

load_dotenv()

API_KEY = os.getenv("API_KEY")
payload = {}
headers = {"apikey": API_KEY}

# currency_code = "RUB"

transactions_operations = way_to_json(json_file)


def currency_conversion(transaction: list[dict[Any, Any]]) -> int | float | str | Any:
    """
    Функция конвертирует валюту и возвращает транзакции в рублях
    """

    list_of_transactions = []
    for transact in transaction:
        operation_amount = transact["operationAmount"]
        if not operation_amount:
            continue

        amount_str = operation_amount["amount"]
        currency = operation_amount["currency"]
        transact_code = currency["code"] if currency else None

        if amount_str is None or transact_code is None:
            continue

        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            continue

        if transact_code in ("USD", "EUR"):
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?"
                f"to=RUB&from={transact_code}&amount={amount}"
            )
            response = requests.get(url, headers=headers, data=payload)
            if response.status_code == 200:
                result = response.json().get("result")
                if isinstance(result, (int, float)):
                    list_of_transactions.append(result)
                    return result
            else:
                return f"Неверный запрос, код ошибки: {response.status_code}"
        elif transact_code == "RUB":
            list_of_transactions.append(amount)
            return amount_str

    return list_of_transactions


conclusion = currency_conversion(transactions_operations)
print(conclusion)
