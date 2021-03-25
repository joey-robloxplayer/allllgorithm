import time




def binary_search(list, item):
    low = 0
    high = len(list)
    while low  <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

tic = time.perf_counter()
my_list = list(range(100000))
item = 99999
print (binary_search(my_list, item)) # => 1
toc = time.perf_counter()

print(f"runtime: {toc - tic:0.7f} seconds")
