#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:05:05 2022

@author: bobrokerson

"""

# Рассмотрим все ту же функцию из задания по линейной алгебре: 
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2), но теперь уже на промежутке [1, 30]
# В первом задании будем искать минимум этой функции на заданном промежутке с помощью scipy.optimize. 
# Разумеется, в дальнейшем вы будете использовать методы оптимизации для более сложных функций,
# а f(x) мы рассмотрим как удобный учебный пример.
# Напишите на Питоне функцию, вычисляющую значение f(x) по известному x. 
# Будьте внимательны: не забывайте про то, что по умолчанию в питоне целые числа делятся нацело, и о том, 
# что функции sin и exp нужно импортировать из модуля math.


from math import sin, exp
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x/ 2.)


xarr = np.arange(1., 31.)
print (xarr)
print ("Shape x:", xarr.shape)
yarr = np.array([func(x) for x in xarr])
print(yarr)
print("Shape y:", yarr.shape)

plt.plot(xarr, yarr)
plt.grid(True)
plt.axis([0, 30, -15, 5])
plt.show()


# Изучите примеры использования  scipy.optimize.minimize в документации Scipy (см. "Материалы")
# Попробуйте найти минимум, используя стандартные параметры в функции  scipy.optimize.minimize 
# (т.е. задав только функцию и начальное приближение). Попробуйте менять начальное приближение и изучить, меняется ли результат. 
# Укажите в scipy.optimize.minimize в качестве метода BFGS (один из самых точных в большинстве случаев градиентных методов оптимизации),
# запустите из начального приближения x=2. Градиент функции при этом указывать не нужно – он будет оценен численно. 
# Полученное значение функции в точке минимума - ваш первый ответ по заданию 1, его надо записать с точностью до 2 знака после запятой.

from scipy.optimize import minimize

minFuncVal = minimize(func, 5)
print ("Min f(x): ", round(minFuncVal.fun,2), "x = ", minFuncVal.x)
print ("Number: ", minFuncVal.nit)


minFuncVal2 = minimize(func, 2, method = 'BFGS')
print ("Min f(x) (BFGS): ", round(minFuncVal2.fun, 2), "for x = ", minFuncVal2.x)
print ("Number: ", minFuncVal2.nit)

minValR1 = np.zeros((2))
minValR1[0] = round(minFuncVal2.fun, 2)
print (minValR1)

# Теперь измените начальное приближение на x=30. Значение функции в точке минимума - ваш второй ответ по заданию 1, 
# его надо записать через пробел после первого, с точностью до 2 знака после запятой.

minFuncVal3 = minimize(func, 30, method = 'BFGS')
print ("Min f(x) (BFGS method): ", minFuncVal3, "for x = ", minFuncVal3.x)
print ("Number: ", minFuncVal3)

minValR1[1] = round(minFuncVal3.fun, 2)
print (minValR1)

minValR1[1] = round(minFuncVal3.fun, 2)
print (minValR1)
