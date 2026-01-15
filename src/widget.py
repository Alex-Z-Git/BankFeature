import re

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
        text: str = ''
        card_number: str = ''
        for symbol in card_data:
            if symbol.isalpha() or symbol == " ":
                text += symbol
            else:
                card_number += symbol
        mask_card_num = get_mask_card_number(card_number)
        return text + mask_card_num


def get_date(some_date: str) -> str:
    match_date = re.search(r"(\d{4})-(\d{2})-(\d{2})", some_date)
    # formatted_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", some_date)
    return f"{match_date.group(3)}.{match_date.group(2)}.{match_date.group(1)}"
#    print(formatted_date)  # 11.03.2024



if __name__ == "__main__":
    print(mask_account_card("Счет 1234567898765432"))
    print(mask_account_card("Visa Master 4567898765432"))
    print(get_date("2024-03-11T02:26:18.671407"))