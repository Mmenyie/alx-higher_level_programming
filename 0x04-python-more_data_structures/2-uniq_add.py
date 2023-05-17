#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_int = set(my_list)
    for num in unique_int:
        result += num
    return result
