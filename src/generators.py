from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> filter:
    """Фильтрует транзакции по валюте и возвращает итератор."""
    return filter(
        lambda t: t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code, transactions
    )


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    """Функция возвращает описание операции"""
    if not transactions:
        return

    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Генератор номеров банковских карт в заданном диапазоне"""
    if not (1 <= start <= stop <= 9999999999999999):
        raise ValueError("Некорректный диапазон номеров карт")

    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        yield " ".join(card_str[i : i + 4] for i in range(0, 16, 4))
