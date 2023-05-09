#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        last digit = 0
    else:
        last_digit = abs(number) % 10
        print(last_digit)
        return last_digit
