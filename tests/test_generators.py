import pytest
from src.generators import filter_by_currency

from tests.conftest import currency_transactions, usd_transactions, eur_transactions

def test_filter_by_currency_usd(currency_transactions, usd_transactions):
    """Проверка при получение  корректных значения для 'USD' """
    assert list(filter_by_currency(currency_transactions, 'USD')) == usd_transactions


def test_filter_by_currency_eur(currency_transactions, eur_transactions):
    """Проверка при получение  корректных значения для 'EUR' """
    assert list(filter_by_currency(currency_transactions, 'EUR')) == eur_transactions


def test_filter_by_currency_empty_list():
    """Проверка на пустой список"""
    assert list(filter_by_currency([], 'USD')) == []


@pytest.mark.parametrize("currency_code, expected", [('RUB', []),
                                                    ('BYR', []),
                                                     ('KZT', []),
                                                     ('', [])])     #отсутствует валюта
def test_filter_by_invalid_currency(currency_transactions, currency_code, expected):
    """Проверка функции при отсутсвие необходимых валют или его отсутсвии"""
    assert list(filter_by_currency(currency_transactions, currency_code)) == expected


