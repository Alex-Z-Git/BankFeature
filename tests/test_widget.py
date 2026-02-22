import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "our_card_data, excepted_card_data",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_basic(our_card_data, excepted_card_data):
    assert mask_account_card(our_card_data) == excepted_card_data


@pytest.mark.parametrize("wrong_type", [("2024/03/11T02:26:18.671407", 13), 20240520, {"a": 24, "b": 12}])
def test_mask_account_wrong_type(wrong_type):
    with pytest.raises(TypeError):
        mask_account_card(wrong_type)


@pytest.mark.parametrize(
    "our_time_data, excepted_our_time_data",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-20T12:01:36.671407", "20.05.2024"),
        ("2025-01-05T14:52:40.671407", "05.01.2025"),
    ],
)
def test_get_date_basic(our_time_data, excepted_our_time_data):
    assert get_date(our_time_data) == excepted_our_time_data


@pytest.mark.parametrize(
    "wrong_time_data, excepted",
    [
        ("2024/03/11T02:26:18.671407", "Введены некорректные параметры времени (ожидается 'YYYY-MM-DD')"),
        ("20240520T12:01:36.671407", "Введены некорректные параметры времени (ожидается 'YYYY-MM-DD')"),
        ("20250614", "Введены некорректные параметры времени (ожидается 'YYYY-MM-DD')"),
    ],
)
def test_get_date_wrong_date(wrong_time_data, excepted):
    assert get_date(wrong_time_data) == excepted


@pytest.mark.parametrize("wrong_type", [("2024/03/11T02:26:18.671407", 13), 20240520, {"a": 24, "b": 12}])
def test_get_date_wrong_type(wrong_type):
    with pytest.raises(TypeError):
        get_date(wrong_type)
