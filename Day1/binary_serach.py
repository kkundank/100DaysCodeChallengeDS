"""
Program find an element in a list Binary Linear Search.

Worst Case: When the given element is not found O(n)
Average Case: Average O(n)
Best Case: Element found at first place O(1)

"""

# TODO again the logic [Not getting it]***


def main():
    list1 = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch(x, list1)
    if result == -1:
        print('Element not found')
    else:
        print(f'Element is: {list1[result]}')


def binarySearch(num, list):
    high = len(list) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < num:
            low = mid + 1
        elif list[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    main()
