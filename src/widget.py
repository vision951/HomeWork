from masks import get_mask_account, get_mask_card_number


def mask_number(account_details: str) -> str:
    """Функция маскирует номер счета или карты в зависимости от типа"""
    # Разделяем входные данные по пробелам
    account_details_list = account_details.split()
    # Проверяем является ли это счетом
    if account_details_list[0].lower() == "счет":
        mask_account = get_mask_account(account_details_list[-1])

        return f"{account_details_list[0].title()} {mask_account}"
    # Если не счет, значит карта
    else:
        mask_card = get_mask_card_number(account_details_list[-1])
        payment_identifier = " ".join(account_details_list[:-1])

        return f"{payment_identifier.title()} {mask_card}"


def get_date(data_time: str) -> str:
    """Функия переформатирования даты"""
    # Разделяем строку по символу T
    date_part = data_time.split("T")[0]
    # Разделяем дату по дефисам
    year, month, day = date_part.split("-")
    # Формируем нужный формат
    return f"{day}.{month}.{year}"


print(mask_number(input("Введите данные")))
print(get_date("2024-03-11T02:26:18.671407"))
