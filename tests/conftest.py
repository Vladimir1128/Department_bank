import pytest


@pytest.fixture
def correct_number():
    return "7000 79** **** 6361"


@pytest.fixture
def incorrect_number():
    return None


@pytest.fixture
def correct_account():
    return "**4305"


@pytest.fixture
def incorrect_account():
    return None