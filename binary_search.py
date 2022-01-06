from random import randint


def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    sorted_list = [i for i in range(randint(10, 100))]
    # sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Length = ', len(sorted_list))
    print(binary_search(sorted_list, 3))
