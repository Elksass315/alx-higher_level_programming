#!/usr/bin/python3

def remove_char_at(str, n):
    output = ""
    for i in range(len(str)):
        if i == n:
            output += ""
        else:
            output += str[i]
    return (output)
