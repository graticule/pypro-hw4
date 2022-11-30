class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.level = 0
        self.current = [iter(self.list_of_list)]
        return self

    def get_next_item(self):
        while True:
            item = next(self.current[self.level])
            if type(item) == list:
                self.level += 1
                self.current.append(iter(item))
            else:
                return item

    def __next__(self):
        while True:
            try:
                item = self.get_next_item()
                return item
            except StopIteration:
                if self.level == 0:
                    raise StopIteration
                del self.current[-1]
                self.level -= 1


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
