#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        sum = 0
        aver = 0
        for element in my_list:
            aver += element[0] * element[1]
            sum += element[1]
        return aver/sum
