#!/usr/bin/python3
def uniq_add(my_list=[]):
    su = 0
    for idx in range(len(my_list)):
        exist = False
        for index in range(idx + 1, len(my_list)):
            if my_list[idx] == my_list[index]:
                exist = True
        if exist is False:
            su += my_list[idx]
    return su
