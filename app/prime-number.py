#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    list_str = sys.argv[1]
    l = [int(x.strip()) for x in list_str.split(',')]
else:
    l = [10, 20, 30, 15, 20, 25, 26]

print(f"Processing list: {l}")

dict_data = {}
for i in l:
    if i in dict_data:
        print(f"Duplicate found: {i}")
    else:
        dict_data[i] = 1

print(f"Final dictionary: {dict_data}")
