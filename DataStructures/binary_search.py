import enum
import random
import time

lst = list(set([random.randint(99, 999) for _ in range(15)]))
print(f"Data Present: {lst}")
sortLst = sorted(lst)
print(f"After Sorting the list: {sortLst}")

def binarySearch(low, high, keyValue):
    while low <= high:
        mid = low + (high - low) // 2
        if keyValue == sortLst[mid]:
            return mid
        elif keyValue > sortLst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

low = 0
high = 14
keyValue = int(input("\nEnter Value to Search: "))
x = binarySearch(low, high, keyValue)
print(x)