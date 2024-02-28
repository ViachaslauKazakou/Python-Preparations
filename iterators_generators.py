import random
import string


def my_generator(length):
    letters = string.ascii_lowercase
    try:
        for i in range(10):
            yield ''.join(random.choice(letters) for _ in range(length))
    except StopIteration:
        print('No more, we reached of end iterator')


def mygenerator2(length):
    letters = string.ascii_lowercase
    return ("".join(random.choice(letters) for _ in range(length)) for _ in range(10))


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration



if __name__ == '__main__':
    try:
        gen = my_generator(10)
        for i, element in enumerate(range(20)):
            # print(gen.__next__())
            print(f'{i} - {next(gen)}')
    except StopIteration:
        print('No more, we reached of end iterator')

    gen2 = mygenerator2(10)
    for i, element in enumerate(gen2):
        print(f'{i} - {element}')

    x = (i for i in range(10))
    for item in x:
        print(item)
    print("-"*100)
    my_list = [1, 2, 3, 4, 5, 6]
    my_iterator = MyIterator(my_list)
    print(next(my_iterator))
    print("------------")
    for item in my_iterator:
        print(item)