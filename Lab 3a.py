#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:47:08 2024

@author: Ruiyang Shi
"""

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.

a = 10

def first_func(b=20):
    c = 30
    d = 40
    value = second_func(b, d, c)
    return value

def second_func(b, d=40, c=0):
    e = 50
    return a + b + c + d + e

result = first_func()
print(result)


#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime

start_dict = {'noah': '2/23/1999', 'sarah': '9/1/2001', 'zach': '8/8/2005'}

def convert_date(date_str):
    month, day, year = map(int, date_str.split('/'))
    return datetime.date(year, month, day)

start_dict = {k: convert_date(v) for k, v in start_dict.items()}

def key_func(k):
    return k.lower()

def val_func(v):
    return v

answer = {key_func(k): val_func(v) for k, v in start_dict.items()}
print(answer)



#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std

from numpy import mean, std

def zscore_series(data):
    data_mean = mean(data)
    data_std = std(data)
    return [(x - data_mean) / data_std for x in data]

values = [1, 2, 3, 4, 5]
print(zscore_series(values))

values = (6, 7, 8, 9, 10) 
print(zscore_series(values))

# 4
from numpy import median, absolute

def zscore_series_mad(data):
    data_median = median(data)
    abs_dev = absolute(data - data_median)
    mad = median(abs_dev)
    return [(x - data_median) / mad for x in data]

values = [1, 2, 3, 4, 5]
print(zscore_series_mad(values))

values = (6, 7, 8, 9, 10) 
print(zscore_series_mad(values))