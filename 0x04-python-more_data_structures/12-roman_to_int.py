#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    elment = [roman_dict[x] for x in roman_string]
    result = 0
    for i in range(len(element)):
        result += element[i]
        if element[i - 1] < element[i] and i != 0:
            result -= (element[i - 1] + element[i - 1])
    return result
