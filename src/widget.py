from masks import get_mask_account, get_mask_card_number

def mask_number(account_details: str) -> str:
    account_details_list = account_details.split()
    if account_details_list[0].lower() == "счет":
        mask_account = get_mask_account(account_details_list[-1])
        return f"{account_details_list[0].title()} {mask_account}"

    else:
        mask_card = get_mask_card_number(account_details_list[-1])
        payment_identifier = " ".join(account_details_list[:-1])
        return f"{payment_identifier.title()} {mask_card}"



print(mask_number(input("Введите данные")))