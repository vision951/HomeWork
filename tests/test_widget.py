import pytest

from src.widget import get_date, mask_number


@pytest.mark.parametrize(
    "account_details, expected",
    [
        ("Счет 125368383", "Счет **8383"),
        ("Счет 368383", "Счет **8383"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_number(account_details, expected):
    """Проверка правильности выполнения корректных данных"""
    assert mask_number(account_details) == expected


def test_mask_number_not_account_details():
    """Проверка на пустую строку"""
    with pytest.raises(ValueError):
        mask_number("")


def test_mask_number_invalid_account_details():
    """Проверка на корректный формат"""
    with pytest.raises(ValueError):
        mask_number("1234123412341234")


def test_mask_invalid_card_type():
    """Проверка на не валидный тип карты"""
    with pytest.raises(ValueError):
        mask_number("Bitcoin 1234567812345678")


@pytest.mark.parametrize(
    "date_time, expected",
    [
        ("2023-12-31T00:00:00", "31.12.2023"),
        ("2000-02-29T12:30:45", "29.02.2000"),  # Високосный год
        ("1990-01-01T23:59:59", "01.01.1990"),  # Проверка формата
        ("2023-01-09T00:00:00", "09.01.2023"),  # Проверка ведущих нулей
    ],
)
def test_get_dates(date_time, expected):
    """Проверка правильности выполнения"""
    assert get_date(date_time) == expected


def test_get_date_empty_string():
    """Проверка на пустую строку"""
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_missing():
    """Проверка обработки строки без даты (только время)"""
    with pytest.raises(ValueError):
        get_date("T12:30:45")
