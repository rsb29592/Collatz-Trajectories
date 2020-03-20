#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
from numpy import savetxt

# Roy Burson
# Date: 9-14-19
# Purpose: To assess my public paper on collatz trajectories
# Descriptions: Collatz research


__author_ = '                            Roy Burson                                    '
__copyright_ = '----------------------@copyright 2019---------------------------------'
import sys
import fileinput

def collatz(number):
    if number % 2 == 0:
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        return result
def average_value_of_array(args):
    length = len(args)
    k = sum(args)
    quoteint = k/length
    return quoteint
# ------------------------------------------------------------------------------------------------
# ------------------------------------List intantiation-------------------------------------------
# ------------------------------------------------------------------------------------------------
x_list = []
y_list = []
trajectory_0mod3 = []
trajectory_2mod3 = []
average_values_of_moduluses = []
# -----------------------------------------------------------------------------------------------
# ------------------------------------Read in data-----------------------------------------------
# -----------------------------------------------------------------------------------------------
y_range = int(input(" Enter max value of domain:"))

# need to condition on input and exit if it is not integer
coefficent = int(input("Enter a coefficent a:"))
intercept = int(input("Enter a intercept b:"))
for n in range(1,y_range):
    x_list.append(n)
    k = coefficent* int(n)+intercept
    trajectory_0mod3 = []
    trajectory_2mod3 = []
    coalescence_list = []
    trajectory_0mod3.append(n)
    trajectory_2mod3.append(k)

    while n != 1:
        n = collatz(int(n))
        trajectory_0mod3.append(n)
    while k != 1:
        k = collatz(int(k))
        trajectory_2mod3.append(k)
    
    if len(trajectory_0mod3)>= len(trajectory_2mod3):
        for i in range(len(trajectory_2mod3)):
            for j in range(len(trajectory_0mod3)):
                if (trajectory_0mod3[j] == trajectory_2mod3[i]):
                    coalescence_point = trajectory_0mod3[j] 
                    coalescence_list.append(coalescence_point)
                    break  
                
    if len(trajectory_2mod3)> len(trajectory_0mod3):
        for i in range(len(trajectory_0mod3)):
            for j in range(len(trajectory_2mod3)):
                if (trajectory_2mod3[j] == trajectory_0mod3[i]):
                    coalescence_point = trajectory_2mod3[j] 
                    coalescence_list.append(coalescence_point)
                    break
                
    if len(coalescence_list) == 0:
        print("sorry there is no intersection point")
        y_list.append(0)
    y_list.append(coalescence_list[0])
    average_values_of_moduluses.append(average_value_of_array(y_list))
xvals=np.array(x_list)

yvals= np.array(y_list)
Z = [(xvals[i], yvals[i]) for i in range(len(xvals))]
savetxt('data.csv', Z, delimiter = ',')
yvals2= np.array(average_values_of_moduluses)
Z2 = [(xvals[i], yvals2[i]) for i in range(len(xvals))]
savetxt('average_value_data.csv', Z2, delimiter = ',')
print(__author_)
print(__copyright_)

