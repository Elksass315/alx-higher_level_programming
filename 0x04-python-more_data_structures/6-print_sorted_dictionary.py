#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    lie = list(a_dictionary.keys())
    lie.sort()
    for i in lie:
        print("{}: {}".format(i, a_dictionary[i]))
