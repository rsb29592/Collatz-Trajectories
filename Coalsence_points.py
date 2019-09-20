#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

# Roy Burson
# Date: 9-14-19
# Purpose: To assess my public paper on collatz trajectories
# Descriptions: Collatz research


__author_ = '                             Roy Burson                                    '
__copyright_ = '-----------------------@copyright 2019---------------------------------'
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


# In[2]:


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

# -----------------------------------------------------------------------------------------------
# -----------------------------------print data -----------------------------------------------
# -----------------------------------------------------------------------------------------------
#print(y_list)
# -----------------------------------------------------------------------------------------------
# ------------------------------------plot data-----------------------------------------------
# -----------------------------------------------------------------------------------------------
yvals= np.array(y_list)
fig = plt.figure(figsize = (8,6))
ax1 = fig.add_axes([0.1,0.1,.8,.8])
ax1.scatter(xvals,yvals, facecolors = 'none', edgecolors = 'k')
ax1.plot(xvals,yvals,c="r",ls='--')    
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_xlabel('n')
ax1.set_ylabel('$T^{k^{\sim}}(n)$')
ax1.tick_params(axis = 'both', which = 'major', labelsize = 12)
fig.tight_layout()
fig.savefig('collatz_scatter1.pdf') 


# In[3]:


# -----------------------------------------------------------------------------------------------
# ----------------------------plot data if a =3 and b =2-----------------------------------------
# -----------------------------------------------------------------------------------------------
if(coefficent == 3 and intercept ==2):
    fig = plt.figure(figsize = (8,6))
    ax1 = fig.add_axes([0.1,0.1,.8,.8])
    ax1.scatter(xvals,yvals, facecolors = 'none', edgecolors = 'k')
    ax1.plot(xvals,yvals,c="r",ls='--')
    ax1.plot([n for n in range(1,y_range)],[(2/3)*n for n in range(1,y_range)],c="k", ls='--')
    ax1.plot([n for n in range(1,y_range)],[(2**2/3**2)*n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[(2**3/3**3)*n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[(2**4/3**4)*n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[(2**5/3**5)*n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[(2**6/3**6)*n for n in range(1,y_range)],c="k",ls='--')
    #ax1.plot([n for n in range(1,y_range)],[(2**7/3**7)*n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[3/2*n for n in range(1,y_range) ],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[3**2/2**2*n for n in range(1,y_range)],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[3**3/2**3*n for n in range(1,y_range) ],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[3**4/2**4*n for n in range(1,y_range) ],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[3**5/2**5*n for n in range(1,y_range) ],c="k",ls='--')
    ax1.plot([n for n in range(1,y_range)],[3**6/2**6*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**7/2**7*n for n in range(1,y_range) ],c="k",ls='--')  
    #ax1.plot([n for n in range(1,y_range)],[3**8/2**8*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**9/2**9*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**10/2**10*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**11/2**11*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**12/2**12*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**14/2**14*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**15/2**15*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.plot([n for n in range(1,y_range)],[3**16/2**16*n for n in range(1,y_range) ],c="k",ls='--') 
    #ax1.set_ylim(1,y_range/2)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.set_xlabel('n')
    ax1.set_ylabel('$T^{k^{\sim}}(n)$')
    ax1.tick_params(axis = 'both', which = 'major', labelsize = 12)
    fig.tight_layout()
    fig.savefig('collatz_scatter1_wlines.pdf') 


# In[4]:


# -----------------------------------------------------------------------------------------------
# ------------------------------------plot eexpected value=--------------------------------------
# -----------------------------------------------------------------------------------------------
fig = plt.figure(figsize = (8,6))
yvals= np.array(average_values_of_moduluses)
fig = plt.figure(figsize = (8,6))
ax1 = fig.add_axes([0.1,0.1,.8,.8])
ax1.scatter(xvals,yvals, facecolors = 'none', edgecolors = 'k')
ax1.plot(xvals,yvals,c="k",ls='--')
if(coefficent == 3 and intercept ==2):
    ax1.plot([n for n in [1,y_range]], [4*n/5 for n in [1,y_range]], c='r', ls ='--')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_xlabel('n')
ax1.set_ylabel('Average value of $T^{k^{\sim}}(n)$')
ax1.tick_params(axis = 'both', which = 'major', labelsize = 12)
fig.tight_layout()
fig.savefig('collatz_expected_value1.pdf') 

