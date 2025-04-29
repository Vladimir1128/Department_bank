import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_correct_1(correct_1):
    assert mask_account_card("Maestro 7000792289606361") == correct_1


def test_mask_account_card_correct_2(correct_2):
    assert mask_account_card("MasterCard 7158300734726758") == correct_2


def test_mask_account_card_correct_3(correct_3):
    assert mask_account_card("Visa Classic 6831982476737658") == correct_3


def test_mask_account_card_correct_4(correct_4):
    assert mask_account_card("Visa Platinum 8990922113665229") == correct_4


def test_mask_account_card_correct_5(correct_5):
    assert mask_account_card("Visa Gold 5999414228426353") == correct_5


def test_mask_account_card_correct_6(correct_6):
    assert mask_account_card("Счет 73654108430135874305") == correct_6

def test_mask_account_card_incorrect_1(incorrect):
    assert mask_account_card("Visa Gold") == incorrect


def test_mask_account_card_incorrect_2(incorrect):
    assert mask_account_card("") == incorrect


def test_mask_account_card_incorrect_3(incorrect):
    assert mask_account_card("VisaGold 73654 1084301 35874305") == incorrect


def test_mask_account_card_incorrect_4(incorrect):
    assert mask_account_card("руский") == incorrect


def test_mask_account_card_incorrect_5():
    with pytest.raises(TypeError):
        mask_account_card()


def test_get_date_correct_date(correct_date):
    assert get_date("2024-03-11T02:26:18.671407") == correct_date


def test_get_date_incorrect_date_1(incorrect_date):
    assert get_date("2024-03-11T02:26:18.67140") == incorrect_date


def test_get_date_incorrect_date_2(incorrect_date):
    assert get_date("aaaa-03-11T02:26:18.671407") == incorrect_date


def test_get_date_incorrect_date_3(incorrect_date):
    assert get_date("02024-03-11T02:26:18.67140") == incorrect_date


def test_get_date_incorrect_date_4(incorrect_date):
    assert get_date("2024-03-11102:26:18.671407") == incorrect_date


def test_get_date_incorrect_date_5(incorrect_date):
    assert get_date("2024-03-11T02:26:18.") == incorrect_date


def test_get_date_incorrect_date_6(incorrect_date):
    assert get_date("2024-03-11T02:26:18.") == incorrect_date


def test_get_date_incorrect_date_7(incorrect_date):
    assert get_date("") == incorrect_date

def test_get_date_incorrect_date_8():
    with pytest.raises(TypeError):
        get_date()


def test_get_date_incorrect_date_9(incorrect_date):
    assert get_date("2024-03-11T02.26:18.671407") == incorrect_date