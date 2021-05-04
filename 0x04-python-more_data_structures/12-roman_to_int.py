#!/usr/bin/python3
def roman_to_int(roman_string):
    data = {'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev, sum = 0, 0
    for x in roman_string[::-1]:
        if data[x] >= prev:
            sum += data[x]
        else:
            sum = sum - data[x]
        prev = data[x]
    return sum
