import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_correct_number(correct_number: str) -> None:
    assert get_mask_card_number(7000792289606361) == correct_number


def test_get_mask_card_number_incorrect_number_1(incorrect_number: None) -> None:
    assert get_mask_card_number(7000792289) == incorrect_number


def test_get_mask_card_number_incorrect_number_2(incorrect_number: None) -> None:
    assert get_mask_card_number(70007922896063610000) == incorrect_number


def test_get_mask_card_number_incorrect_number_3(incorrect_number: None) -> None:
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_card_number_incorrect_number_4(incorrect_number: None) -> None:
    assert get_mask_card_number("aaaaaaaaaaaaaaaa") == incorrect_number


def test_get_mask_card_number_incorrect_number_5(incorrect_number: None) -> None:
    assert get_mask_card_number("AAAAAAAA") == incorrect_number


def test_get_mask_card_number_incorrect_number_6(incorrect_number: None) -> None:
    assert get_mask_card_number(12345678901234) == incorrect_number


def test_get_mask_card_number_incorrect_number_7(incorrect_number: None) -> None:
    assert get_mask_card_number("  ") == incorrect_number


def test_get_mask_account_correct_account(correct_account: str) -> None:
    assert get_mask_account(73654108430135874305) == correct_account


def test_get_mask_account_incorrect_account_1(incorrect_account: None) -> None:
    assert get_mask_account(73654108430) == incorrect_account


def test_get_mask_account_incorrect_account_2(incorrect_account: None) -> None:
    assert get_mask_account(736541084301358743050000) == incorrect_account


def test_get_mask_account_incorrect_account_3(incorrect_account: None) -> None:
    with pytest.raises(TypeError):
        get_mask_account()


def test_get_mask_account_incorrect_account_4(incorrect_account: None) -> None:
    assert get_mask_account("aaaaaaaaaaaaaaaaaaaa") == incorrect_account


def test_get_mask_account_incorrect_account_5(incorrect_account: None) -> None:
    assert get_mask_account("AAAAAAAA") == incorrect_account


def test_get_mask_account_incorrect_account_6(incorrect_account: None) -> None:
    assert get_mask_account(12345678901234) == incorrect_account


def test_get_mask_account_incorrect_account_7(incorrect_account: None) -> None:
    assert get_mask_account("  ") == incorrect_account
