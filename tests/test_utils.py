import pytest
from unittest.mock import patch, mock_open
import json

from src.utils import load_transactions


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "state": "EXECUTED"}]))
def test_load_transactions_success(mock_file):
    """Тест успешной загрузки транзакции из файла"""
    result = load_transactions("dummy_path.json")
    assert result == [{"id": 1, "state": "EXECUTED"}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_transactions_file_not_found(mock_file):
    """Тест обработки ошибки, когда файл не найден"""
    result = load_transactions("nonexistent_file.json")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="{invalid_json}")
def test_load_transactions_invalid_json(mock_file):
    """Тест обработки невалидного json"""
    result = load_transactions("invalid.json")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"id": 1, "state": "EXECUTED"}))
def test_load_transactions_success(mock_file):
    """Тест успешной загрузки транзакции из файла"""
    result = load_transactions("not_a_list.json")
    assert result == []




