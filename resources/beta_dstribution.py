#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:37:59 2022

@author: jimmy
"""
# Beta destribution

import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
%matplotlib inline

a, b = 7, 3

beta_rv = sts.beta(a, b)
sample = beta_rv.rvs(50)

# plt.plot(sample)
sample[:10]


plt.hist(sample, density=True, bins = 20)

x = np.linspace(0,1,100)
pdf = beta_rv.pdf(x)
plt.plot(x, pdf)

plt.ylabel('histogram vs theoretical PDF')
plt.xlabel('$x$')

m = a / (a + b)
D = a*b / (a+b)**2 / (a+b+1)
sigma = np.sqrt(D)

m, sigma


# checking theorem

n = 5
all_samples_of_n = []
for i in range(1000):
    all_samples_of_n.append(np.random.choice(sample, n))
means = np.array([s.mean() for s in all_samples_of_n])  
plt.hist(means, density=True, bins = 30)
plt.ylabel('PDF')
plt.xlabel('$mean$')    

x = np.linspace(0,1,100)
norm_rv = sts.norm(loc=m, scale = sigma/2)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)

norm_rv_unscaled = sts.norm(loc=m, scale = sigma)
pdf = norm_rv_unscaled.pdf(x)
plt.plot(x, pdf)

plt.xlim(0.4,0.9)

print('Approximate value: ', round(m,4), round(means.mean(),4))

print('Beta distribution', round(sigma/2, 4),  round(np.std(means),4))


n = 20
all_samples_of_n = []
for i in range(1000):
    all_samples_of_n.append(np.random.choice(sample, n))
means = np.array([s.mean() for s in all_samples_of_n])    
plt.hist(means, density=True, bins = 30)
plt.ylabel('PDF')
plt.xlabel('$mean$') 

x = np.linspace(0,1,100)
norm_rv = sts.norm(loc=m, scale = sigma/4)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)

plt.xlim(0.6,0.95)

n = 50
all_samples_of_n = []
for i in range(1000):
    all_samples_of_n.append(np.random.choice(sample, n))
means = np.array([s.mean() for s in all_samples_of_n])    
plt.hist(means, density=True, bins = 22)
plt.ylabel('PDF')
plt.xlabel('$mean$') 

x = np.linspace(0,1,100)
norm_rv = sts.norm(loc=m, scale = sigma/7)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)
plt.xlim(0.6,0.8)



