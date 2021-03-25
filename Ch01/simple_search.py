import time



def simple_search(list, item):
    for i in range(0 , len(list)):
        if list[i] == item:
            return i
    return None
    
tic = time.perf_counter()
my_list = list(range(160_000_000))
item = 159_999_999
print (simple_search(my_list, item)) # => 1
toc = time.perf_counter()

print(f"runtime: {toc - tic:0.3f} seconds")
