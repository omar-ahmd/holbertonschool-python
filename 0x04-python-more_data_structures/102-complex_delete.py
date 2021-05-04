#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, element in a_dictionary.copy().items():
        if element == value:
            del a_dictionary[key]
    return a_dictionary
