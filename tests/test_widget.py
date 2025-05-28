import pytest

from src.widget import mask_number
from tests.conftest import number_card


@pytest.mark.parametrize("account_details, expected",[('Счет 125368383', 'Счет **8383'),
                                         ('Счет 368383', 'Счет **8383'),
                                         ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                         ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361')])
def test_mask_number(account_details, expected):
    assert mask_number(account_details) == expected

# проверка на пустую строку
def test_mask_number_not_account_details():
    with pytest.raises(ValueError):
        mask_number('')

# проверка на корректный формат
def test_mask_number_invalid_account_details():
    with pytest.raises(ValueError):
        mask_number('1234123412341234')

# проверка на не валидный тип карты
def test_mask_invalid_card_type():
    with pytest.raises(ValueError):
        mask_number("Bitcoin 1234567812345678")