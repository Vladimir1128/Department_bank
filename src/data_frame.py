import json
from typing import Any

import pandas as pd


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


if __name__ == "__main__":
    data_csv = "data/transactions.csv"
    print(my_csv(data_csv))
    data_excel = "data/transactions_excel.xlsx"
    print(my_excel(data_excel))
