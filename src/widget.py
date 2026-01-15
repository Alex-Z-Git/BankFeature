from masks import get_mask_account
from masks import  get_mask_card_number

def mask_account_card(card_data: str) -> str:
    """Функция выдающая замаскированную карту"""
    if "Счет" in card_data:
        text: str = ''
        bill_number: str = ''
        for symbol in card_data:
            if symbol.isalpha() or symbol == " ":
                text += symbol
            else:
                bill_number += symbol
        mask_bill_num = get_mask_account(bill_number)
        return text + mask_bill_num

    else:

        print("No")
    return "Opa"

if __name__ == "__main__":
    print(mask_account_card("Счет 1234567898765432"))
    mask_account_card("Visa 4567898765432")