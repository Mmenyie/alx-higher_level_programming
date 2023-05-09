#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        last digit = 0
    else:
        last_digit = abs(number) % 10
        print(f'{last_digit}', end, end='')
        return last_digit
