import re

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_data: str) -> str:
    """Функция выдающая замаскированную карту"""
    if "Счет" in card_data:
        bill_text: str = ''
        bill_number: str = ''
        for symbol in card_data:
            if symbol.isalpha() or symbol == " ":
                bill_text += symbol
            else:
                bill_number += symbol
        mask_bill_num = get_mask_account(bill_number)
        return bill_text + mask_bill_num

    else:
        card_text: str = ''
        card_number: str = ''
        for symbol in card_data:
            if symbol.isalpha() or symbol == " ":
                card_text += symbol
            else:
                card_number += symbol
        mask_card_num = get_mask_card_number(card_number)
        return card_text + mask_card_num


def get_date(some_date: str) -> str:
    match_date = re.search(r"(\d{4})-(\d{2})-(\d{2})", some_date)
    if match_date:
        #  formatted_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", some_date)
        return (f"{match_date.group(3)}.{match_date.group(2)}.{match_date.group(1)}")
    else:
        return "Введены некорректные параметры времени (ожидается 'YYYY-MM-DD')"
#    print(formatted_date)  # 11.03.2024


if __name__ == "__main__":

    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print()

    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("2024-03/11T02:26:18.671407"))
