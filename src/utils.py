import json
import logging
from typing import Any

way_to_json_logger = logging.getLogger("app.way_json")
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
way_to_json_logger.addHandler(file_handler)
way_to_json_logger.setLevel(logging.DEBUG)


def way_to_json(json_file: str) -> list[Any]:
    """
    Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    way_to_json_logger.info("Starts work!")
    try:
        with open(json_file, encoding="utf-8") as file_in:
            data = json.load(file_in)

        if isinstance(data, list):
            way_to_json_logger.info("Program works correctly!")
            return data
        else:
            way_to_json_logger.warning("Unsuccessful  program termination!")
            return []
    except FileNotFoundError as e:
        way_to_json_logger.error(f"An error occurred!: {e}")
        return []
    except json.JSONDecodeError as e:
        way_to_json_logger.error(f"An error occurred!: {e}")
        return []
    finally:
        way_to_json_logger.info("Completion of work!")


if __name__ == "__main__":
    transactions_ = way_to_json("data/operations.json")
    print(transactions_)
