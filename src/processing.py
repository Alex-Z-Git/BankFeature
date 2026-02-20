from typing import Iterable


def filter_by_state(list_dict: Iterable, state_value: str = "EXECUTED") -> Iterable:
    """Функция сортирующая список по значению state ('EXECUTED' по умолчанию)"""
    if isinstance(list_dict, list):
        if list_dict == []:
            raise ValueError("Ошибка. Передан пустой список")

        filtered_list = []
        for itm in list_dict:
            for key, value in itm.items():
                if key == "state" and value == state_value:
                    filtered_list.append(itm)

    else:
        raise TypeError("Неверные данные для сортировки (ожидается список словарей)")
    if filtered_list == []:
        raise ValueError("Ошибка. В переданном списке словарей отсутствует ключ 'state' "
                         "либо его значение передано неверно")
    return filtered_list


def sort_by_date(list_dictionary: Iterable, direction: bool = True) -> Iterable:
    """Функция сортирующая список словарей по значению "date" и возвращающая новый отсортированный список
    Направление сортировки задается параметром 'direction' True (по умолчанию) - убывание, False - возрастание"""
    if isinstance(list_dictionary, list):
        if list_dictionary == []:
            raise ValueError("Ошибка. Передан пустой список")
        if not isinstance(direction, bool):
            raise TypeError("Ошибка. Укажите направление сортировки 'True' or 'False' или не передавайте его")
        try:
            new_sorted_list = sorted(list_dictionary, key=lambda x: x["date"], reverse=direction)
        except KeyError:
            raise ValueError("Ошибка. В переданном списке нет словарей с ключом 'date' ")
    else:
        raise TypeError("Неверные данные для сортировки (ожидается список словарей)")
    return new_sorted_list


# if __name__ == "__main__":
#
# try: number = int(input("Введите число: ")) print(f"Вы ввели: {number}")
# except ValueError: print("Ошибка: нужно ввести число!")
#     our_list = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#
#     # print(sort_by_date(our_list))
#     date_list = sort_by_date(our_list)
#
#     for i in date_list:  # Выводим лист построчно для удобства проверки
#         print(i)
#
#     print()
#
#     date_list = sort_by_date(our_list, False)  # Меняем направление сортировки.
#
#     for i in date_list:  # Выводим лист построчно для удобства проверки
#         print(i)
#
#     print()
#
#     date_list = sort_by_date(our_list, 1)  # Меняем направление сортировки.
#
#     for i in date_list:  # Выводим лист построчно для удобства проверки
#         print(i)

    # print()  # Печатаем пустую строку для форматирования вывода
    # print(filter_by_state(our_list, "CANCELED"))  # выводим отфильтрованный список
    # print()  # Печатаем пустую строку для форматирования вывода
    # print(filter_by_state(our_list, "EXECUTED"))  # Меняем параметр фильтрования
    # print()  # Печатаем пустую строку для форматирования вывода
    # print(filter_by_state(our_list, "EXeeECUTED"))  # Меняем параметр фильтрования
    # print()  # Печатаем пустую строку для форматирования вывода
    # #print(filter_by_state([], "EXECUTED"))  # Меняем параметр фильтрования
    # print()  # Печатаем пустую строку для форматирования вывода
    # print(filter_by_state([{"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
    #     {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "date": "2018-10-14T08:21:33.419441"}], "EXECUTED"))  # Меняем параметр фильтрования
