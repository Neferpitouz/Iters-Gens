class MyMassive:

    def __init__(self, ex_list):
        self.ex_list = ex_list
        self.count = len(ex_list)
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.pointer = -1
        return self

    def __next__(self):
        if self.pointer == len(self.ex_list[self.cursor]) - 1:
            iter(self)
        if self.cursor == self.count:
            raise StopIteration
        self.pointer += 1
        return self.ex_list[self.cursor][self.pointer]


def flat_generator(ex_list):
    cursor = 0
    pointer = 0
    while cursor <= len(ex_list):
        if pointer == len(ex_list[cursor]):
            pointer = 0
            cursor += 1
            if cursor == len(ex_list):
                break
        result = ex_list[cursor][pointer]
        pointer += 1
        yield result


my_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

new_list = MyMassive(my_list)
if __name__ == '__main__':
    for item in new_list:
        print(item)
    print()
    for item in flat_generator(my_list):
        print(item)
