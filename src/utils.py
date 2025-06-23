import json


def load_transactions(file_path: str)-> list[dict]:
    """Загружает данные о транзакциях с json файла"""
    try:
       with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return []
    return data if isinstance(data, list) else []

