import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

json_file = "data/operations.json"

load_dotenv()

API_KEY = os.getenv("API_KEY")
payload = {}
headers = {"apikey": API_KEY}

currency_code = "RUB"

with open(json_file, encoding="utf-8") as file:
    transactions_operations = json.load(file)


def currency_conversion(transaction: list[dict[Any, Any]], code: str) -> list[float] | str:
    """
    Функция конвертирует валюту и возвращает транзакции в рублях
    """
    list_of_transactions = []
    for transact in transaction:
        operation_amount = transact.get("operationAmount")
        if not operation_amount:
            continue

        amount_str = operation_amount.get("amount")
        currency = operation_amount.get("currency")
        transact_code = currency.get("code") if currency else None

        if amount_str is None or transact_code is None:
            continue

        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            continue

        if transact_code in ("USD", "EUR"):
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?"
                f"to={code}&from={transact_code}&amount={amount}"
            )
            response = requests.get(url, headers=headers, data=payload)
            if response.status_code == 200:
                result = response.json().get("result")
                if isinstance(result, (int, float)):
                    list_of_transactions.append(result)
            else:
                return f"Неверный запрос, код ошибки: {response.status_code}"
        elif transact_code == code:
            list_of_transactions.append(amount)

    return list_of_transactions


conclusion = currency_conversion(transactions_operations, "USD")
print(conclusion)
