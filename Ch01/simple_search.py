def simple_search(list, item):
    for i in range(0 , len(list)):
        if list[i] == item:
            return i
    return None
    





my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
print (simple_search(my_list, -0)) # => 1
