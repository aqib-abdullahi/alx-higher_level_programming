#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if len(my_list) > 0:
        i = 0
        j = 0
        for i in my_list:
            if my_list[j] == search:
                new_list[j] = replace

            j += 1
    return new_list
