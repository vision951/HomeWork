import pytest
from unittest.mock import patch, Mock

from src.external_api import convert_transaction_to_rub


def test_convert_transaction_to_rub_rub():
    """Тест конвертации транзакции в рублях (без конвертации)"""
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_transaction_to_rub(transaction)
    assert result == 100.0


@patch("requests.get")
def test_convert_transaction_to_rub_usd_success(mock_get):
    """Тест успешной конвертации USD в  RUB"""
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "rates": {"RUB": 75.0}
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = convert_transaction_to_rub(transaction)
    assert result == 7500.0


@patch("requests.get", side_effect=Exception("API Error"))
def test_convert_transaction_to_rub_api_invalid(mock_get):
    """Тест обработки ошибки API"""
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    result = convert_transaction_to_rub(transaction)
    assert result == 0.0


def test_convert_transaction_to_invalid_structure():
    """Тест обработки неверной структуры транзакции"""
    transaction = {"invalid" : "structure"}
    result = convert_transaction_to_rub(transaction)
    assert result == 0.0


def test_convert_transaction_to_invalid_amount():
    """Тест обработки неверного формату суммы"""
    transaction = {
        "operationAmount": {
            "amount": "lol",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_transaction_to_rub(transaction)
    assert result == 0.0


def test_convert_transaction_empty():
    """Тест обработки пустой транзакции"""
    transaction = {}
    result = convert_transaction_to_rub(transaction)
    assert result == 0.0

