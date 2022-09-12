nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# 1. Реализация через класс:
class FlatIterator:

    def __init__(self, iter_object):
        self.iter_object = iter_object
        self.current = 0

    def __iter__(self):
        self.iter_object2 = [el for i in self.iter_object for el in i]
        return self

    def __next__(self):
        if self.current < len(self.iter_object2):
            result = self.iter_object2[self.current]
            self.current += 1
            return result
        raise StopIteration


# 2. Реализация через генератор:
def flat_generator(iter_object):
    count = 0
    while count < len(iter_object):
        internal_count = 0
        while internal_count < len(iter_object[count]):
            yield iter_object[count][internal_count]
            internal_count += 1
        count += 1


# 3. Итератор для списков любого уровня вложенности:
nested_list2 = [
    ['a', 'b', ['g', 'k', 3, 4], 'c'],
    [[False, None, 6, 'l', ['m', 'o']], 'd', 'e', 'f', 'h', False],
    [1, 2, None]
]
nested_list3 = [
    ['a', 'b', ['g', 'k', 3, 4], 'c'],
    [[False, None, 6, 'l', ['m', 'o']], 'd', 'e', 'f', 'h', False],
    [1, 2, None]
]


class DeepIterator:

    def __init__(self, iter_object):
        self.iter_object = iter_object
        self.current = 0

    def __iter__(self):
        self.new_list = []
        while len(self.iter_object):
            el = self.iter_object.pop()
            for x in el:
                if type(x) is list:
                    self.iter_object.append(x)
                else:
                    self.new_list.append(x)
        return self

    def __next__(self):
        if self.current < len(self.new_list):
            result = self.new_list[self.current]
            self.current += 1
            return result
        raise StopIteration


# 4. Генератор для списков любого уровня вложенности:
nested_list4 = [
    ['a', 'b', ['g', 'k', 3, 4], 'c'],
    [[False, None, 6, 'l', ['m', 'o']], 'd', 'e', 'f', 'h', False],
    [1, 2, None]
]
nested_list5 = [
    ['a', 'b', ['g', 'k', 3, 4], 'c'],
    [[False, None, 6, 'l', ['m', 'o']], 'd', 'e', 'f', 'h', False],
    [1, 2, None]
]


def deep_generator(iter_object):
    while len(iter_object):
        el = iter_object.pop()
        for x in el:
            if type(x) is list:
                iter_object.append(x)
            else:
                yield x


flat_it1 = FlatIterator(nested_list)
flat_list1 = [item for item in FlatIterator(nested_list)]
flat_list2 = [item for item in flat_generator(nested_list)]

flat_it2 = DeepIterator(nested_list2)
flat_list3 = [item for item in DeepIterator(nested_list3)]
flat_list4 = [item for item in deep_generator(nested_list5)]

if __name__ == '__main__':
    for item in flat_it1:
        print(item)
    print(flat_list1)
    for item in flat_generator(nested_list):
        print(item)
    print(flat_list2)
    for item in flat_it2:
        print(item)
    print(flat_list3)
    for item in deep_generator(nested_list4):
        print(item)
    print(flat_list4)

