#!/usr/bin/python3


def to_subtract(list_num):
    to = 0
    mx = max(list_num)

    for i in list_num:
        if mx > i:
            to += i

    return (mx - to)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(romdic.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in keys:
            if r_num == ch:
                if romdic.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [romdic.get(ch)]
                else:
                    list_num.append(romdic.get(ch))

                last_rom = romdic.get(ch)

    num += to_subtract(list_num)

    return (num)
