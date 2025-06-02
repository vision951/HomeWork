def filter_by_currency(transactions: list[dict], currency_code: str) -> filter:
    """Фильтрует транзакции по валюте и возвращает итератор."""
    return filter(
        lambda t: t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code,
        transactions
    )


