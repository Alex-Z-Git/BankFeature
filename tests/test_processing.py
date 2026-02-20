import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def our_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


@pytest.fixture
def excepted_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


def test_filter_by_state_basic(our_list, excepted_list):

    assert filter_by_state(our_list) == excepted_list


def test_filter_by_state_zero():

    with pytest.raises(ValueError):
        filter_by_state([])


@pytest.fixture
def our_list_without_state():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_without_state(our_list_without_state, excepted_list):
    with pytest.raises(ValueError):
        filter_by_state(our_list_without_state)


@pytest.mark.parametrize("state_value", ["defrua", 1234, ("ex", "can")])
def test_filter_by_state_wrong_data(our_list, state_value):
    with pytest.raises(ValueError):
        filter_by_state(our_list, state_value)


@pytest.mark.parametrize("wrong_list", ["defrua", 1234, {"ex", "can"}, (1, 3, 5), 23.89])
def test_filter_by_state_wrong_input_data(wrong_list):
    with pytest.raises(TypeError):
        filter_by_state(wrong_list)


@pytest.fixture
def expected_date_list():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_sort_by_date_basic(our_list, expected_date_list):

    assert sort_by_date(our_list) == expected_date_list


def test_sort_by_date_zero():

    with pytest.raises(ValueError):
        sort_by_date([])


@pytest.mark.parametrize("direction", ["defrua", 1234, ("ex", "can")])
def test_sort_by_date_wrong_direction_data(our_list, direction):
    with pytest.raises(TypeError):
        sort_by_date(our_list, direction)


@pytest.mark.parametrize("wrong_list", ["defrua", 1234, {"ex", "can"}, (1, 3, 5), 23.89])
def test_sort_by_date_wrong_input_data(wrong_list):
    with pytest.raises(TypeError):
        sort_by_date(wrong_list)


@pytest.fixture
def our_list_without_date():
    return [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
        {"id": 615064591, "state": "CANCELED"}
    ]


def test_sort_by_date_without_date(our_list_without_date, expected_date_list):
    with pytest.raises(ValueError):
        sort_by_date(our_list_without_date)
