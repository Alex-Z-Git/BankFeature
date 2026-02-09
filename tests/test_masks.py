import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [(1234567898765432, "1234 56** **** 5432"),
                                                   ("9876543223456789", "9876 54** **** 6789"),
                                                   ("1234 5678 9876 0123", "1234 56** **** 0123")
                                                   ])
def test_get_mask_card_number_basic(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [1234567765,
                                         4345657687767464345434557656,
                                         "9876 54** **** 6789",
                                         "asdfghjkllkjhgfd",
                                         [9876, 5432, 1098, 7654],
                                         "1234:5678:8765:4321"
                                         ])
def test_get_mask_card_number_wrong_values(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("bill_number, expected", [(98765432112345675432, "**5432"),
                                                   ("12345678998765436789", "**6789"),
                                                   ("1234 5678 5555 9876 0123", "**0123")
                                                   ])
def test_get_mask_account_basic(bill_number, expected):
    assert get_mask_account(bill_number) == expected


@pytest.mark.parametrize("bill_number", [1234567765,
                                         4345657687767464345434557656,
                                         "9876 54** **** 6789",
                                         "asdfghjkllkjhgfddjhf",
                                         [9876, 5432, 1098, 7654],
                                         "1234:5678:8765:4321:5647"
                                         ])
def test_get_mask_account_wrong_values(bill_number):
    with pytest.raises(ValueError):
        get_mask_account(bill_number)
