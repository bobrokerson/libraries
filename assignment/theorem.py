#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:58:59 2022

@author: bobrokerson
"""

%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
from math import sqrt

# parameters
xx = 5.0
yy = 4.0


#frozen distribution
distribution = sts.pareto(xx, loc=0, scale=yy)

# generation 1000
distribution1 = distribution.rvs(1000)
print('Theoretical mean: ', distribution.mean())
print('Standard deviation: ', round(distribution.std(),20))


# histogram
plt.hist(distribution1, bins=30, density=True, label='PDF')

# theoretical distribution density
x = np.linspace(0,20,1000)
pdf = distribution.pdf(x)
plt.plot(x, pdf, label='Theoretical PDF')
plt.legend()
plt.grid()
plt.axis([0, 12, 0, 2])
plt.title('Pareto probability distribution function')


# generation 
number = 1000

# array
xarr = [5, 10, 50]

# array for the sample average value
distribution1 = np.zeros( (len(xarr), number) )

# calculation of sample averages and entering into an array
for i in range( len(xarr) ):
    for j in range(number):
        distribution1Temp = np.array( sts.pareto.rvs(xx, loc=0, scale=yy, size=xarr[i]) )
        distribution1TempMean = distribution1Temp.mean()
        distribution1[i, j] = distribution1TempMean
        
print(distribution1)



# Math expectation and dispersion

distribution1Mean = xx * yy / (xx - 1)
distribution1Var = np.zeros(len(xarr))
for i in range(len(xarr)):
    distribution1Var[i] = yy**2 * xx / ( (xx - 1)**2 * (xx - 2) ) / xarr[i]
    
print( 'Math expectation: ' + str(distribution1Mean))
for i in range(len(xarr)):
    print(' Dispersion for n = ' + str(xarr[i]) + ': ' + str(distribution1Var[i]))
    
# approximation
for i in range(len(xarr)):
    plt.hist(distribution1[i], bins=30, density=True)
    plt.grid()
    plt.axis([2, 8, 0, 3])
    plt.title('Pareto probability distribution function for n = ' + str(xarr[i]))
    plt.xlabel('x')
    plt.ylabel('pdf')

    mu = distribution1Mean
    sigma = sqrt(distribution1Var[i])
    k = sts.norm(loc=mu, scale=sigma)    
    x = np.linspace(-10,10,1000)
    pdf = k.pdf(x)
    plt.plot(x, pdf)
    plt.show()
    
for i in range(len(xarr)):
    plt.hist(distribution1[i], bins=30, density=True, label='n = ' + str(xarr[i]))
    plt.grid()
    plt.axis([2, 8, 0, 3])
    plt.title('Pareto probability distribution function')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('pdf')
    
    mu = distribution1Mean
    sigma = sqrt(distribution1Var[i])
    k = sts.norm(loc=mu, scale=sigma)    
    x = np.linspace(-10,10,1000)
    pdf = k.pdf(x)
    plt.plot(x, pdf)
    
# conclusion: as n increasing, the accuracy of the normal approximation're increasing as well