"""
Program find an element in a list using Linear Search.

Worst Case: When the given element is not found O(n)
Average Case: Average O(n)
Best Case: Element found at first place O(1)

"""


def main():
    list1 = [2, 3, 4, 5, 6]
    x = 3
    result = linearSearch(x, list1)
    if result == -1:
        print('Element not found')
    else:
        print(f'Element is: {result}')


def linearSearch(num, all_num):
    for i in all_num:
        if i == num:
            return i
    return -1


if __name__ == '__main__':
    main()
