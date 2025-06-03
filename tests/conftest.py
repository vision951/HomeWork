import pytest


@pytest.fixture
def number_card():
    return 1234123412341234


@pytest.fixture
def transactions_example():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 5, "state": "PENDING", "date": "2018-05-12T21:27:25.241689"},
        {"id": 6, "state": "APPROVED", "date": "2018-12-14T08:21:33.419441"},
    ]


@pytest.fixture
def expected_executed():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def expected_canceled():
    return [
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_not_state():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_sort_asc():
    return [
        {"id": 5, "state": "PENDING", "date": "2018-05-12T21:27:25.241689"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 6, "state": "APPROVED", "date": "2018-12-14T08:21:33.419441"},
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def transactions_sort_desc():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 6, "state": "APPROVED", "date": "2018-12-14T08:21:33.419441"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 5, "state": "PENDING", "date": "2018-05-12T21:27:25.241689"},
    ]


@pytest.fixture
def transactions_same_date():
    return [
        {"date": "2023-01-01T12:00:00", "id": 1},
        {"date": "2023-01-01T11:00:00", "id": 2},
        {"date": "2023-01-01T10:00:00", "id": 3},
    ]


@pytest.fixture
def gen_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {"amount": "500.00", "currency": {"code": "EUR"}},
            "description": "Покупка в магазине",
        },
    ]


@pytest.fixture
def usd_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
    ]


@pytest.fixture
def eur_transactions():
    return [
        {
            "id": 873106923,
            "operationAmount": {"amount": "500.00", "currency": {"code": "EUR"}},
            "description": "Покупка в магазине",
        }
    ]
