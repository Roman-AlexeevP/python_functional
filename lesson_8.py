import functools

example = [1, 2, 3, 5, 6]
example2 = [1, 2, 3, 5, 6, 6]


def second_max(array):
    largest = functools.reduce(
            lambda x,y: x if x > y else y,
            array
    )
    if array.count(largest) > 1:
        return largest
    return functools.reduce(
            lambda x,y: x if y < x < largest or y == largest else y,
            array
    )
if __name__ == '__main__':

    print(second_max(example)) # 5
    print(second_max(example2)) # 6
