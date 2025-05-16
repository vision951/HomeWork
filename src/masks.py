def get_mask_card_number(number_card: str) -> str:
    """функция маскировки номера банковской карты"""

    # Проверяем, что номер состоит из цифр
    if not number_card.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    # Проверяем длину номера карты
    if len(number_card) != 16:
        raise ValueError("Некорректная длина номера карты")

    # Разделеям номер карты по блокам из 4 цифр
    blocks_number = [number_card[i:i + 4] for i in range(0, len(number_card), 4)]

    # Маскируем блоки
    masked_blocks = [blocks_number[0], blocks_number[1][:2] + "**", "****", blocks_number[-1]]
    return " ".join(masked_blocks)


def get_mask_account(account_number: str) -> str:
    """функция маскировки номера счета"""

    # Проверяем, что номер состоит из цифр
    if not account_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    return f"**{account_number[-4:]}"


# print(get_mask_card_number(input("Введите номер карты")))
# print(get_mask_account(input("Введите номер счета")))
