import random
import time

lst = list(set([random.randint(99, 999) for _ in range(20)]))
print(f"Data Present: {lst}")
keyValue = int(input("\nEnter Value to Search: "))
start = time.time()
for index, value in enumerate(lst):
    if value == keyValue:
        print("Value Present at Index {}.".format(index))

end = time.time()-start
print(f"Time taken {round(end, 5)}s.")