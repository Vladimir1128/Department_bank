from unittest.mock import patch

from src.external_api import API_KEY, currency_conversion

headers = {"apikey": API_KEY}


@patch('requests.get')
def test_currency_conversion_1(mock_request):
    test_1 = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    code_1 = "RUB"
    transaction_code = test_1[0]["operationAmount"]["currency"]["code"]
    amount = float(test_1[0]["operationAmount"]["amount"])

    mock_request.return_value.json.return_value = {"result": 8221.37}
    mock_request.return_value.status_code = 200
    assert currency_conversion(test_1) == 8221.37
    print(mock_request.return_value.json.return_value)
    mock_request.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to={code_1}&from={transaction_code}&amount={amount}",
        headers=headers,
        data={}
    )
