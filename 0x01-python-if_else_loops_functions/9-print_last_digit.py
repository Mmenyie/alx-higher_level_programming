#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    last_digit = number % 10
    print(f"{last_digit}", end='')
    return last_digit
