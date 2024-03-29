#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:11:09 2024

@author: Ruiyang Shi
"""

# 1
x = int('10')
y = 20
print(x + y)

# 2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len - 1])

# 3
my_string = 'hello world'
print(my_string.upper())

# 4
z = ['a', 'b', 'c']
z.append('d')
print(z) 

# 5
x = 10
y = 20
print(x * y)


# 6
blue = "blue"
color = 'My favorite color is {}, what is yours?'.format(blue)
print(color)

# 7
yellow = "yellow"
color = 'My favorite color is {}, what is yours?'.format(yellow)
print(color)

# 8
red = "red"
color = f'My favorite color is {red}, what is yours?'
print(color)

# 9
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools = list(set(schools))

# 10
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = list(animals)
animals[animals.index('dog')] = 'cat'
animals = tuple(animals)

# 11
my_sent = 'All that snow we had this winter sure was fun!'
my_sent = [word.lower() for word in my_sent.split()]