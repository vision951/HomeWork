import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("number_card, expected",[('1234123412341234', '1234 12** **** 1234'),
                                                  ('4321432143214321', '4321 43** **** 4321')])
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected


@pytest.mark.parametrize("number_card", ('ghshshdhsdh',
                                         '1233hkhyf',
                                         '123412341234123'))
def test_get_mask_card_number_invalid_type_card(number_card):
    with pytest.raises(ValueError):
        get_mask_card_number(number_card)


def test_get_mask_card_number_invalid_empty_str():
    with pytest.raises(ValueError):
        get_mask_card_number('')


@pytest.mark.parametrize("account_number, expected",[('1234123412341234', '**1234'),
                                                  ('43214321', '**4321'),
                                                     ('101010', '**1010')])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number",['12345',
                                          '12345hgk',
                                          'ghslsdjk',
                                           ''])
def test_get_mask_account_invalid_type_account(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


