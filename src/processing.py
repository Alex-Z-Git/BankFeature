from typing import Iterable

def filter_by_state(list_dict: Iterable, state='EXECUTED')-> Iterable:

    filtered_list = []
    for i in list_dict:
        for key, value in i.items():
            if value == state:
                filtered_list.append(i)


    return filtered_list




def sort_by_date(list_dictions: Iterable, direction: bool = True) -> Iterable:
    """Функция сортирующая список словарей по значению "date" и возвращающая новый отсортированный список"""
    """Направление сортировки задается параметром 'direction' True (по умолчанию) - убывание, False - возрастание """

    new_sorted_list = sorted(list_dictions, key = lambda x: x['date'], reverse = direction)


    return new_sorted_list


if __name__ == "__main__":


    our_list = [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                ]

    print(sort_by_date(our_list))
    print(filter_by_state(our_list))