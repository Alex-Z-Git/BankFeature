import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transaction_list():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def excepted_rub_list():
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def excepted_usd_list():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


def test_filter_by_currency_rub(transaction_list, excepted_rub_list):
    generator = filter_by_currency(transaction_list, "RUB")
    assert next(generator) == excepted_rub_list[0]
    assert next(generator) == excepted_rub_list[1]
    assert next(generator) == "Конец списка"


def test_filter_by_currency_usd(transaction_list, excepted_usd_list):
    generator = filter_by_currency(transaction_list, "USD")
    assert next(generator) == excepted_usd_list[0]
    assert next(generator) == excepted_usd_list[1]
    assert next(generator) == excepted_usd_list[2]
    assert next(generator) == "Конец списка"


def test_filter_by_currency_no_rub(excepted_usd_list):
    generator = filter_by_currency(excepted_usd_list, "RUB")
    assert next(generator) == "Выбранная валюта в списке отсутствует или список пуст"
    assert next(generator) == "Выбранная валюта в списке отсутствует или список пуст"


def test_filter_by_currency_zero():
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Выбранная валюта в списке отсутствует или список пуст"
    assert next(generator) == "Выбранная валюта в списке отсутствует или список пуст"


@pytest.fixture
def transaction_description_list():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_normal(transaction_list, transaction_description_list):
    generator = transaction_descriptions(transaction_list)
    assert next(generator) == transaction_description_list[0]
    assert next(generator) == transaction_description_list[1]
    assert next(generator) == transaction_description_list[2]
    assert next(generator) == transaction_description_list[3]
    assert next(generator) == transaction_description_list[4]
    assert next(generator) == "Список транзакций исчерпан"


def test_transaction_descriptions_zero():
    generator = transaction_descriptions([])
    assert next(generator) == "В списке нет описания транзакции. (Отсутствует ключ 'description') "


def test_transaction_descriptions_part(transaction_list, transaction_description_list):
    generator = transaction_descriptions(transaction_list)
    assert next(generator) == transaction_description_list[0]
    assert next(generator) == transaction_description_list[1]
    assert next(generator) == transaction_description_list[2]


@pytest.fixture
def card_number_list_1_5():
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_normal(card_number_list_1_5):
    generator = card_number_generator(1, 5)
    assert next(generator) == card_number_list_1_5[0]
    assert next(generator) == card_number_list_1_5[1]
    assert next(generator) == card_number_list_1_5[2]
    assert next(generator) == card_number_list_1_5[3]
    assert next(generator) == card_number_list_1_5[4]
    assert next(generator) == "Все карты заданного диапазона сгенерированы"


def test_card_number_generator_max():
    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"


def test_card_number_generator_one(card_number_list_1_5):
    generator = card_number_generator(1, 1)
    assert next(generator) == card_number_list_1_5[0]


def test_card_number_generator_over():
    generator = card_number_generator(9999999999999999, 10000000000000009)
    assert next(generator) == "Ошибка. Значения не могут быть больше 9'999'999'999'999'999"


def test_card_number_generator_start_lower_end():
    generator = card_number_generator(9999999999999999, 1000000000000009)
    assert next(generator) == "Ошибка. Конечное число меньше начального"


def test_card_number_generator_lower():
    generator = card_number_generator(-2, 109)
    assert next(generator) == "Ошибка. Значения должны быть положительными"
