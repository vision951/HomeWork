import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_transaction_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакций в рубли"""
    # Если пустой список транзакций
    if not transaction:
        return 0.0
    try:
        # Получаем информацию о сумме и валюте транзакции
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        # Если валюта в рублях
        if currency == 'RUB':
            return amount

        if currency in ('USD', 'EUR'):
            params = {'from': currency, 'to': 'RUB', 'amount': amount}
            headers = {'apikey': API_KEY}

            response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            print("Ответ API:", data)

            if data.get('success', False):
                return data['result']

    except KeyError as e:
        print(f"Ошибка в структуре транзакции: {e}")
    except ValueError as e:
        print(f"Ошибка преобразования суммы: {e}")
    except requests.RequestException as e:
        print(f"Ошибка запроса к API: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

    return 0.0
