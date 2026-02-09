from typing import Union




def get_mask_card_number(number: Union[int, str]) -> str:
    """Функция, которая принимает номер карты в виде числа или строки
     и возвращает замаскированный номер карты вида '7000 79** **** 6361' """

    temp_number = str(number)
    formated_temp_number = temp_number.replace(" ", "")

    if formated_temp_number.isdigit() and len(formated_temp_number) == 16:

        mask_number = formated_temp_number[:4] + " " + formated_temp_number[4:6] + "**" + " **** " + formated_temp_number[-4:]

    else:
        raise ValueError("Неверный формат данных")

    return mask_number


def get_mask_account(bill: Union[int, str]) -> str:
    """Функция, которая принимает номер счета в виде числа или строки
    и возвращает замаскированный номер счета вида '**6361' """

    temp_bill = str(bill)
    formated_temp_bill = temp_bill.replace(" ", "")

    if formated_temp_bill.isdigit() and len(formated_temp_bill) == 20:
        mask_bill = "**" + temp_bill[-4:]
    else:
        raise ValueError("Неверный формат данных")

    return mask_bill


if __name__ == "__main__":
    print(get_mask_card_number(1234567898765432))
    print(get_mask_card_number("1234 5678 9876 5432"))

    print(get_mask_account(73654108430135874305))
    print(get_mask_account("12345678998765432100"))
