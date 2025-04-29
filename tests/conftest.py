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



@pytest.fixture
def correct_1():
    return "Maestro 7000 79** **** 6361"


@pytest.fixture
def correct_2():
    return "MasterCard 7158 30** **** 6758"


@pytest.fixture
def correct_3():
    return "Visa Classic 6831 98** **** 7658"


@pytest.fixture
def correct_4():
    return "Visa Platinum 8990 92** **** 5229"


@pytest.fixture
def correct_5():
    return "Visa Gold 5999 41** **** 6353"


@pytest.fixture
def correct_6():
    return "Счет **4305"


@pytest.fixture
def incorrect():
    return "Неправильно введены данные!"

@pytest.fixture
def correct_date():
    return "11.03.2024"


@pytest.fixture
def incorrect_date():
    return "Неправильно введены данные!"