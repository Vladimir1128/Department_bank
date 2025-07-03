import json
from typing import Any


def way_to_json(json_file: str) -> list[Any]:
    """
    Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(json_file, encoding="utf-8") as file_in:
            data = json.load(file_in)

        if isinstance(data, list):
            return data
        else:
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    transactions_ = way_to_json("data/operations.json")
    print(transactions_)

