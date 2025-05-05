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


@pytest.mark.parametrize('number, expected',
                         [("Visa Gold", "Неправильно введены данные!"), ("", "Неправильно введены данные!"),
                          ("VisaGold 73654 1084301 35874305", "Неправильно введены данные!"),
                          ("русcкий", "Неправильно введены данные!"),
                          ("Виза Голд 5999414228426353", "Неправильно введены данные!")])
def test_mask_account_card_incorrect(number, expected):
    assert mask_account_card(number) == expected


def test_mask_account_card_incorrect_5():
    with pytest.raises(TypeError):
        mask_account_card()


def test_get_date_correct_date(correct_date):
    assert get_date("2024-03-11T02:26:18.671407") == correct_date


@pytest.mark.parametrize('date, expected', [("2024-03-11T02:26:18.6714070", "Неправильная длина данных!"),
                                            ("aaaa-03-11T02:26:18.671407", "Неправильно введены данные!"),
                                            ("02024-03-11T02:26:18.67140", "Неправильно введены данные!"),
                                            ("2024-03-11102:26:18.671407", "Неправильно введены данные!"),
                                            ("2024-03-11T02:26:18.", "Неправильная длина данных!"),
                                            ("", "Неправильно введены данные!"),
                                            ("2024-03-00T02:26:18.671407", "Неправильно введена дата!"),
                                            ("2024-03-32T02:26:18.671407", "Неправильно введена дата!"),
                                            ("2024-00-11T02:26:18.671407", "Месяц указан неверно"),
                                            ("2024-13-11T02:26:18.671407", "Месяц указан неверно"),
                                            ("0000-01-11T02:26:18.671407", "Год указан неверно"),
                                            ("9001-01-11T02:26:18.671407", "Год указан неверно"),
                                            ("2024-02-30T02:26:18.671407", "Неправильно введена дата!"),
                                            ])
def test_get_date_incorrect_date(date, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(date)
    assert str(exc_info.value) == expected


def test_get_date_incorrect_date_8():
    with pytest.raises(TypeError):
        get_date()
