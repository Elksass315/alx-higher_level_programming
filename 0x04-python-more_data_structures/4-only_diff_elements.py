#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    lie = []

    for i in set_1:
        if i not in set_2:
            lie.append(i)

    for i in set_2:
        if i not in set_1 and i not in lie:
            lie.append(i)
    return lie
