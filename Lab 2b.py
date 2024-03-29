#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:29:13 2024

@author: Ruiyang Shi
"""
# 1
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    elif i < 5:
        print('little')
    elif i >= 5:
        print('big')
    else:
        print('what happened?')
    print('Finished!')
    i += 1

# 2
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
    
# 3
start_list = [[2, 3, 4], [6, 8, 9]]
flattened_and_filtered_list_comprehension = [item - 1 for sublist in start_list for item in sublist if item - 1 <= 4]
print(flattened_and_filtered_list_comprehension)

# 4
import datetime

start_dict = {
    'noah': '2/23/1999',
    'sarah': '9/1/2001',
    'zach': '8/8/2005'
}
formatted_dict_comprehension = {
    name.capitalize(): datetime.datetime.strptime(date_string, '%m/%d/%Y') for name, date_string in start_dict.items()
}
print(formatted_dict_comprehension)