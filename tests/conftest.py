import pytest


@pytest.fixture
def correct_number() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def incorrect_number() -> None:
    return None


@pytest.fixture
def correct_account() -> str:
    return "**4305"


@pytest.fixture
def incorrect_account() -> None:
    return None


@pytest.fixture
def correct_date() -> str:
    return "11.03.2024"


@pytest.fixture
def variable_1() -> list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def variable_2() -> list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "PROCESSING", "date": "2017-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "PROCESSING", "date": "2021-05-30T02:08:58.425572"},
        {"id": 594226727, "state": "ACTIVE", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "ACTIVE", "date": "2018-11-14T08:21:33.419441"},
    ]


@pytest.fixture
def variable_3() -> list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T02:08:58.425572"},
    ]


@pytest.fixture
def variable_4() -> list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2020-01-01T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2024-02-29T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-12-31T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-02-28T08:21:33.419441"},
    ]
