#!/usr/bin/python3
for i in range(122, 64, -1):
    if i % 2 == 0:
        char = chr(i).upper()
    else:
        char = chr(i)
    print(char, end='')
