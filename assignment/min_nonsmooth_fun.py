#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:36:06 2022

@author: bobrokerson
"""
# part of code from task #1

from math import sin, exp
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x/ 2.)


xarr = np.arange(1., 31.)
print(xarr)
print("x:", xarr.shape)
yarr = np.array([func(x) for x in xarr])
print(yarr)
print("y:", yarr.shape)

plt.plot(xarr, yarr)
plt.grid(True)
plt.axis([0, 30, -15, 5])
plt.show()


# 1.Теперь рассмотрим функцию h(x) = int(f(x)) на том же отрезке [1, 30], т.е. теперь каждое значение f(x) приводится к типу int и функция принимает только целые значения.
# 2.Такая функция будет негладкой и даже разрывной, а ее график будет иметь ступенчатый вид. Убедитесь в этом, построив график h(x) с помощью matplotlib.
# 3.Попробуйте найти минимум функции h(x) с помощью BFGS, взяв в качестве начального приближения x=30. Получившееся значение функции – ваш первый ответ в этой задаче.
# 4.Теперь попробуйте найти минимум h(x) на отрезке [1, 30] с помощью дифференциальной эволюции. Значение функции h(x) в точке минимума – это ваш второй ответ в этом задании. Запишите его через пробел после предыдущего.
# 5.Обратите внимание на то, что полученные ответы различаются. Это ожидаемый результат, ведь BFGS использует градиент (в одномерном случае – производную) и явно не пригоден для минимизации рассмотренной нами разрывной функции. Попробуйте понять, почему минимум, найденный BFGS, именно такой (возможно в этом вам поможет выбор разных начальных приближений).
# 6.Выполнив это задание, вы увидели на практике, чем поиск минимума функции отличается от глобальной оптимизации, и когда может быть полезно применить вместо градиентного метода оптимизации метод, не использующий градиент. Кроме того, вы попрактиковались в использовании библиотеки SciPy для решения оптимизационных задач, и теперь знаете, насколько это просто и удобно.

from scipy.optimize import minimize
from scipy.optimize import differential_evolution

def funcnew(x): 
    return int(func(x))

xarrnew = np.arange(1., 31., 0.01)
print(xarrnew)
print("x:", xarrnew.shape)
yarrnew = np.array([funcnew(x) for x in xarrnew])
print(yarrnew)
print("y:", yarrnew.shape)

# create plot
plt.plot(xarrnew, yarrnew)
plt.grid(True)
plt.axis([0, 30, -15, 5])
plt.show()


minFuncnewVal1 = minimize(funcnew, 30, method = 'BFGS')
print("Min f(x) BFGS method: ", round(minFuncnewVal1.fun, 3), "for x = ", minFuncnewVal1.x)
print("Number: ", minFuncnewVal1.nit)

minValR2 = np.zeros( (2) )
minValR2 [0] = round(minFuncnewVal1.fun, 2)
print(minValR2)

# searching min h(x)

bounds = [(1, 30)]
minFuncnewVal2 = differential_evolution(funcnew, bounds)
print("Min f(x) BFGS method: ", round(minFuncnewVal2.fun, 3), "for x = ", minFuncnewVal2.x)
print("Number: ", minFuncnewVal2.nit)

minValR2[1] = round(minFuncnewVal2.fun, 2)
print (minValR2)

with open("docvalue3.txt", "w") as file:
    for item in minValR2:
        file.write(str(item) + ' ')
        S
