from src.masks import get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_card_number_1():
    assert get_mask_card_number(7000792289) == None


def test_get_mask_card_number_2():
    assert get_mask_card_number(70007922896063610000) == None


def test_get_mask_card_number_3():
    assert get_mask_card_number() == None


def test_get_mask_card_number_4():
    assert get_mask_card_number("aaaaaaaaaaaaaaaa") == None

def test_get_mask_card_number_4():
    assert get_mask_card_number("AAAAAAAA") == None


def test_get_mask_card_number_4():
    assert get_mask_card_number(  12345678901234) == None


def test_get_mask_card_number_5():
    assert get_mask_card_number("  ") == None