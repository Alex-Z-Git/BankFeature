from typing import Union


def get_mask_card_number(number: Union[int, str]) -> str:
    """Функция котрорая принимает номер карты ввиде числа или строки"""
    """ и возвращает замаскированный номер карты вида "7000 79** **** 6361" """

    temp_number = str(number)
    mask_number = temp_number[:4] + " " + temp_number[4:6] + "**" + " **** " + temp_number[-4:]

    return mask_number


def get_mask_account(bill: Union[int, str]) -> str:
    """Функция котрорая принимает номер счета ввиде числа или строки"""
    """ и возвращает замаскированный номер счета вида " **6361 " """

    temp_bill = str(bill)
    mask_bill = "**" + temp_bill[-4:]

    return mask_bill


if __name__ == "__main__":
    print(get_mask_card_number(1234567898765432))
    print(get_mask_account(73654108430135874305))
