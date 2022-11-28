class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_number = 0
        self.element_number = -1
        return self

    def __get_next(self):
        is_found = False
        while not is_found and self.list_number < len(self.list_of_list):
            self.element_number += 1
            if self.element_number >= len(self.list_of_list[self.list_number]):
                self.list_number += 1
                self.element_number = -1
            else:
                is_found = True
        return is_found

    def __next__(self):
        if self.__get_next():
            item = self.list_of_list[self.list_number][self.element_number]
            return item
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
