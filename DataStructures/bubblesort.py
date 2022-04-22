import random
from re import L
import time

lst = list(set([random.randint(99, 999) for _ in range(15)]))
print(f"Data Present: {lst}")

def bubble_sort(lst):
    sorted = True
    for r in range(len(lst)-1):
        for i in range(len(lst)-1-r):
            if (lst[i] > lst[i+1]) and (sorted):
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                sorted = False
 
    return lst, sorted

lst, sorted = bubble_sort(lst)
if sorted:
    print("List is Already Sorted.")
else:
    print("list is not Sorted.")