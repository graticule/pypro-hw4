class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.level = 0
        self.element_number = [-1]
        return self

    def __get_element(self, indexes):
        result = self.list_of_list
        for i in indexes:
            result = result[i]
        return result

    def __get_next(self):
        is_found = False
        while (not is_found) and self.level >= 0:
            self.element_number[self.level] += 1
            current_list = self.__get_element(self.element_number[:-1])
            if self.element_number[self.level] >= len(current_list):
                del self.element_number[self.level]
                self.level -= 1
            else:
                current_element = self.__get_element(self.element_number)
                if type(current_element) == list:
                    self.level += 1
                    self.element_number.append(-1)
                else:
                    is_found = True
        return is_found

    def __next__(self):
        if self.__get_next():
            item = self.__get_element(self.element_number)
            return item
        else:
            raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
