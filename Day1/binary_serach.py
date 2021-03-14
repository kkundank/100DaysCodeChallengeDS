"""
Program find an element in a list Binary Linear Search.

Worst Case: O(logn)
Average Case: O(logn)
Best Case: O(1), This happen if the element that element we are looking find in the first comparison.
Note: The elements in the list must be sorted to apply the binary search algorithm.
Two Ways: Iterative and Recursive
"""

# TODO again the logic [Not getting it]***


def main():
    list1 = [12, 24, 32, 39, 45, 50, 54]
    x = 32
    resultItr = binarySearchItr(x, list1)
    resultRec = binarySearchRec(x, 0, len(list1)-1, list1)
    if resultItr == -1:
        print('Element not found')
    else:
        print(f'Element is using Itr function: {list1[resultItr]}')
    if resultRec == -1:
        print('Element not found using Rec function')
    else:
        print(f'Element is using Rec function: {list1[resultRec]}')


def binarySearchItr(num, list):
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


def binarySearchRec(num, low, high, list):

    if low <= high:
        mid = (low + high) // 2
        if num == list[mid]:
            return mid
        elif num < list[mid]:
            return binarySearchRec(num, low, mid-1, list)
        else:
            return binarySearchRec(num, mid+1, high, list)
    else:
        return -1


if __name__ == '__main__':
    main()
