from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


VALID_CARD_TYPES = {"visa", "mastercard", "maestro", "мир"}

def mask_number(account_details: str) -> str:
    """Функция маскирует номер счета или карты в зависимости от типа"""

    # Проверка на пустую строку
    if not account_details:
        raise ValueError("Пустая строка")

    # Разделяем входные данные по пробелам
    parts = account_details.split()

    # проверка на корректность формата
    if len(parts) < 2:
        raise ValueError("Некорректный формат: ожидается 'Тип Номер'")

    try:
        # Проверяем является ли это счетом
        if parts[0].lower() == "счет":
            mask_account = get_mask_account(parts[-1])

            return f"{parts[0].title()} {mask_account}"

        # Проверка, является ли тип карты допустимым
        is_valid_card = False
        for card_type in VALID_CARD_TYPES:
            if card_type in parts[0].lower():
                is_valid_card = True
                break
        # Если карта допустима, маскируем
        if is_valid_card:
            masked_number = get_mask_card_number(parts[-1])
            card_name = " ".join(parts[:-1])  # название карты
            return f"{card_name} {masked_number}"

        else:
            raise ValueError("Неизвестный тип карты")

    except ValueError as e:
        raise ValueError(f"Ошибка маскировки: {e}")


def get_date(data_time: str) -> str:
    """Функия переформатирования даты"""

    try:
        # Разделяем строку по символу T
        date_part = data_time.split("T")[0]
        # Парсим дату по формату ГГГГ-ММ-ДД
        date_obj = datetime.strptime(date_part, "%Y-%m-%d")
        # Формируем нужный формат
        return date_obj.strftime("%d.%m.%Y")

    except (IndexError, ValueError):
        #  Выдаем информацию об ошибке
        raise ValueError(f"Некорректный формат даты: {data_time}")




