import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import (expected_executed, expected_canceled,
                            transactions_example, transactions_not_state, \
                             transactions_same_date)


def test_filter_by_state_executed(transactions_example, expected_executed):
    """проверка по значению по умолчанию"""
    assert filter_by_state(transactions_example) == expected_executed


def test_filter_by_state_canceled(transactions_example, expected_canceled):
    """проверка по  значению 'CANCELED'"""
    assert filter_by_state(transactions_example, "CANCELED") == expected_canceled


def test_filter_by_not_state(transactions_not_state):
    """проверка на пустую строку"""
    assert filter_by_state(transactions_not_state) == []


@pytest.mark.parametrize("state, expected_ids", [("EXECUTED", [1, 2]),
                                                ("CANCELED", [3, 4]),
                                                ("PENDING", [5]),
                                                ("APPROVED", [6]),
                                                ("UNKNOWN", []),  # несуществующий
                                                ("EXECUTE", []),  # похожее слово           # Часть слова
                                                ("PEND", [])])    # неполное слово
def test_filter_by_state(transactions_example, state, expected_ids):
    """Параметризованный тест фильтрации по разным статусам"""
    result = filter_by_state(transactions_example, state)
    result_ids = [t["id"] for t in result]
    assert result_ids == expected_ids


def test_sort_by_date_desc(transactions_example, transactions_sort_desc):
    """Проверка сортировки по убыванию"""
    assert sort_by_date(transactions_example) == transactions_sort_desc


def test_sort_by_date_asc(transactions_example, transactions_sort_asc):
    """Проверка сортировки по возрастанию"""
    assert sort_by_date(transactions_example, reverse_sort=False) == transactions_sort_asc


def test_sort_by_same_date(transactions_same_date):
    """Проверка коректности сортировки с одинаковыми датами"""
    assert sort_by_date(transactions_same_date) == transactions_same_date


def test_sort_by_date_empty_list():
    """Проверка пустого списка транзакций"""
    assert sort_by_date([]) == []


def test_sort_by_date_empty_date_string():
    """Проверка обработки пустой строки в дате"""
    with pytest.raises(ValueError):
        sort_by_date([{"date": "", "id": 1}])


def test_sort_by_date_missing_date_key():
    """Проверка обработки отсутствия ключа date"""
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])



