def selection_sort(array: list) -> list:
    size = len(array)
    if not size:
        return []

    for index in range(size):
        min_value = array[index]
        min_index = index

        for jndex in range(index, size):
            if array[jndex] < min_value:
                min_value = array[jndex]
                min_index = jndex

        if min_index != index:
            array[index], array[min_index] = array[min_index], array[index]

    return array


if __name__ == '__main__':
    import random
    randomlist = []
    for i in range(0, 10):
        n = random.randint(1, 30)
        randomlist.append(n)
    print(selection_sort(randomlist))
