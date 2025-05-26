def filter_by_state(transactions: list, state: str ='EXECUTED') ->list:
    """Функция фильтрации словарей по ключу"""
    filtered_list = []

    # Перебираем все транзакции в цикле
    for transaction in transactions:
        # Проверяем наличие ключа 'state'
        if 'state' in transaction:
            # Проверяем соответствие значения ключа 'state'
            if transaction['state'] == state:
                # Добавляем подходящую транзакцию в новый список
                filtered_list.append(transaction)

    return filtered_list

def sort_by_date(transactions: list, reverse_sort: bool = True) -> list:
    """Сортирует список транзакций по дате"""
    return sorted(
        transactions,
        key=lambda x: x["date"].split("T")[0],
        reverse=reverse_sort
    )
