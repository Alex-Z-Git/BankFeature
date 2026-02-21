from typing import Any, Iterable


def filter_by_currency(transactions_list: Iterable, money: str) -> Iterable :
    """Функция фильтрующая список транзакций по названию валюты в ключе 'code' """
    # result = []
    # for value in transactions:
    #     if money == value.get("operationAmount", {}).get("currency", {}).get("code", "Not Found"):
    #         result.append(value)
    # if result:

    result = [value for value in transactions_list
              if money == value.get("operationAmount", {}).get("currency", {}).get("code", "Not Found")]

    if result:
        for item in result:
            yield item
    else:
        while True:
            yield "Выбранная валюта в списке отсутствует или список пуст"

    while True:
        yield "Конец списка"


def transaction_descriptions(trans_list: Iterable) -> Any:
    """Функция-генератор возвращающая описание транзакции из ключа 'description' """
    result = [x for x in trans_list for key, value in x.items() if key == "description"]

    if result:
        for item in result:
            for key, value in item.items():
                if key == "description":
                    yield value

        while True:
            yield "Список транзакций исчерпан"

    else:
        while True:
            yield "В списке нет описания транзакции. (Отсутствует ключ 'description') "


def card_number_generator(start_num: int, end_num: int) -> Any:
    """Функция-генератор для создания номеров карт в заданном диапазоне
    возвращает номера карт в формате '0000 0000 0000 1234' """
    start_x = int(start_num)
    end_x = int(end_num)
    if end_x < start_x:
        while True:
            yield "Ошибка. Конечное число меньше начального"
    elif start_x < 0 or end_x < 0:
        while True:
            yield "Ошибка. Значения должны быть положительными"
    elif start_x > 9999999999999999 or end_x > 9999999999999999:
        while True:
            yield "Ошибка. Значения не могут быть больше 9'999'999'999'999'999"
    else:
        num = start_x
        for i in range(start_x, end_x + 1):
            num_str = f'{num:016d}'
            yield (' '.join([num_str[i:i + 4] for i in range(0, 16, 4)]))
            num += 1
        while True:
            yield "Все карты заданного диапазона сгенерированы"

# if __name__ == "__main__":
#     for card_number in card_number_generator(9, 99999999999999999):
#         print(card_number)
#
#     for card_number in card_number_generator(987123456, 987123459):
#         print(card_number)
#
#     transactions = (
#         [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {
#                     "amount": "9824.07",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702"
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {
#                     "amount": "79114.93",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188"
#             },
#             {
#                 "id": 873106923,
#                 "state": "EXECUTED",
#                 "date": "2019-03-23T01:09:46.296404",
#                 "operationAmount": {
#                     "amount": "43318.34",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 44812258784861134719",
#                 "to": "Счет 74489636417521191160"
#             },
#             {
#                 "id": 895315941,
#                 "state": "EXECUTED",
#                 "date": "2018-08-19T04:27:37.904916",
#                 "operationAmount": {
#                     "amount": "56883.54",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Classic 6831982476737658",
#                 "to": "Visa Platinum 8990922113665229"
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {
#                     "amount": "67314.70",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Visa Platinum 1246377376343588",
#                 "to": "Счет 14211924144426031657"
#             }
#         ]
#     )
#
#     us = filter_by_currency(transactions, "RUB")
#     print(next(us))
#     print(next(us))
#     print(next(us))
#     print(next(us))
#     print(next(us))
#
#     # transact = []
#     # description = transaction_descriptions(transact)
#     # print(next(description))
#     #
#     # description = transaction_descriptions(transactions)
#     # print(next(description))
#     #
#     # print(next(description))
#     # print(next(description))
#     #
#     # print(next(description))
#     # print(next(description))
#     #
#     # print(next(description))
#     # print(next(description))
#     #
#     # print(next(description))
