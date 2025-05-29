import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
                "EXECUTED",
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        ),
        (
                "CANCELED",
                [
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
        ),
    ],
)
def test_filter_by_state_by_default_1(
        state: str,
        variable_1: list[dict[str, str | int]],
        expected: list[dict[str, str | int] | dict[str, str | int]] | list[
            dict[str, str | int] | dict[str, str | int]], ) -> None:
    assert filter_by_state(variable_1, state) == expected


@pytest.mark.parametrize(
    "state, expected",
    [
        (
                "PROCESSING",
                [],
        ),
        (
                "ACTIVE",
                [],
        ),
        (
                "DENIED",
                [],
        ),
    ],
)
def test_filter_by_state_by_default_2(state: str, variable_1: list[dict[str, str | int]], expected: list) -> None:
    assert filter_by_state(variable_1, state) == expected


def test_filter_by_state_by_default_3() -> None:
    assert filter_by_state([]) == []


@pytest.mark.parametrize(
    "state, expected",
    [
        (
                "PROCESSING",
                [
                    {"id": 41428829, "state": "PROCESSING", "date": "2017-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "PROCESSING", "date": "2021-05-30T02:08:58.425572"},
                ],
        ),
        (
                "ACTIVE",
                [
                    {"id": 594226727, "state": "ACTIVE", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "ACTIVE", "date": "2018-11-14T08:21:33.419441"},
                ],
        ),
    ],
)
def test_filter_by_state_by_default_4(
        state: str,
        variable_2: list[dict[str, str | int]],
        expected: list[dict[str, str | int] | dict[str, str | int]] | list[
            dict[str, str | int] | dict[str, str | int]], ) -> None:
    assert filter_by_state(variable_2, state) == expected


@pytest.mark.parametrize(
    "revers, expected",
    [
        (
                True,
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        ),
        (
                False,
                [
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                ],
        ),
    ],
)
def test_sort_by_date_sort_1(
        variable_1: list[dict[str, str | int]],
        revers: bool,
        expected: (
                list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]
                | list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]
        ),
) -> None:
    assert sort_by_date(variable_1, revers) == expected


@pytest.mark.parametrize(
    "revers, expected",
    [
        (
                True,
                [
                    {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T21:27:25.241689"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T02:08:58.425572"},
                ],
        ),
        (
                False,
                [
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T02:08:58.425572"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T18:35:29.512364"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T21:27:25.241689"},
                ],
        ),
    ],
)
def test_sort_by_date_same_date(
        variable_3: list[dict[str, str | int]],
        revers: bool,
        expected: (
                list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]
                | list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]
        ),
) -> None:
    assert sort_by_date(variable_3, revers) == expected


@pytest.mark.parametrize(
    "revers, expected",
    [
        (
                True,
                [
                    {"id": 939719570, "state": "EXECUTED", "date": "2024-02-29T02:08:58.425572"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2020-01-01T18:35:29.512364"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-12-31T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-02-28T08:21:33.419441"},
                ],
        ),
        (
                False,
                [
                    {"id": 615064591, "state": "CANCELED", "date": "2018-02-28T08:21:33.419441"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-12-31T21:27:25.241689"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2020-01-01T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2024-02-29T02:08:58.425572"},
                ],
        ),
    ],
)
def test_sort_by_date_sort_2(
        variable_4: list[dict[str, str | int]],
        revers: bool,
        expected: (
                list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]
                | list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]
        ),
) -> None:
    assert sort_by_date(variable_4, revers) == expected
