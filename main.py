def selection_sort(array: list):
    size = len(array)

    for index in range(size):
        min_value = array[index]
        min_index = index

        for jndex in range(index + 1, size):
            if array[jndex] < min_value:
                min_value = array[jndex]
                min_index = jndex

        if min_index != index:
            array[index], array[min_index] = array[min_index], array[index]


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    selection_sort(randomlist)
    print(randomlist)
