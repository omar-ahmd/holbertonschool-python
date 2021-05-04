#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in set(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
