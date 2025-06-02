import pytest
from src.generators import filter_by_currency, transaction_descriptions

from tests.conftest import gen_transactions, usd_transactions, eur_transactions

def test_filter_by_currency_usd(gen_transactions, usd_transactions):
    """Проверка при получение  корректных значения для 'USD' """
    assert list(filter_by_currency(gen_transactions, 'USD')) == usd_transactions


def test_filter_by_currency_eur(gen_transactions, eur_transactions):
    """Проверка при получение  корректных значения для 'EUR' """
    assert list(filter_by_currency(gen_transactions, 'EUR')) == eur_transactions


def test_filter_by_currency_empty_list():
    """Проверка на пустой список"""
    assert list(filter_by_currency([], 'USD')) == []


@pytest.mark.parametrize("currency_code, expected", [('RUB', []),
                                                    ('BYR', []),
                                                     ('KZT', []),
                                                     ('', [])])     #отсутствует валюта
def test_filter_by_invalid_currency(gen_transactions, currency_code, expected):
    """Проверка функции при отсутсвие необходимых валют или его отсутсвии"""
    assert list(filter_by_currency(gen_transactions, currency_code)) == expected


def test_transaction_descriptions(gen_transactions):
    """Проверка генератора при получении корректных данных"""
    generator = transaction_descriptions(gen_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Покупка в магазине"


def test_transaction_descriptions_empty_input():
    """Проверка функции при отсутсвии транзакции"""
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions_missing_key():
    """Проверка обработки транзакций без ключа 'description'"""
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100.00"}},
        {"id": 2, "date": "2023-01-01T12:00:00"},
        {"id": 3}
    ]

    generator = transaction_descriptions(transactions)
    assert next(generator) == "Описание отсутствует"
    assert next(generator) == "Описание отсутствует"
    assert next(generator) == "Описание отсутствует"



