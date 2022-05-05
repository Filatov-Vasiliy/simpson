import numpy as np
from math import sqrt, cos


# функция округления до кратного 4
def n_mod4(n):
    while n % 4 != 0:
        n = n + 1
    return n


e = 0.001  # точность
a = 0.6  # нижняя граница
b = 2.2  # верхняя граница
n_first = round((b - a) / (e ** 0.25))
n = n_mod4(n_first)  # число итераций
h = round((b - a) / n, 5)  # шаг интегрирования
# Значения x d в пределах от a до b с шагом h
x = np.arange(a, b, h).tolist()

fx = []

# y - заданная функция, fx список значений
for i in x:
    y = cos(i)/(i**2+1)
    fx.append(y)

I_sum_even = 0
I_sum_odd = 0
fx2 = []
for i in range(0, len(fx)):
    if i % 2 == 1 and i != len(fx)-1:
        I_sum_odd += fx[i]  # сумма на нечетных позициях
    if i % 2 == 0 and i != len(fx)-1 and i != 0:
        I_sum_even += fx[i]  # сумма на четных позициях
    if i % 2 == 0 and i != len(fx)-1 and i != 0:
        fx2.append(fx[i])  # список для решения второго интеграла

I1 = h / 3 * (fx[0] + fx[len(fx)-1] + 4 * I_sum_odd + 2 * I_sum_even)  # Приближенное значение интеграла

I2_sum_even = 0
I2_sum_odd = 0

for i in range(0, len(fx2)):
    if i % 2 == 1:
        I2_sum_even += fx2[i]
    if i % 2 == 0:
        I2_sum_odd += fx2[i]

I2 = 2 * h / 3 * (fx[0] + fx[len(fx)-1] + 4 * I2_sum_odd + 2 * I2_sum_even)  # приближенное значение интеграла с шагом 2h

print('Значение интеграла, с шагом h = ', I1)
print('Значение интеграла, с шагом 2h = ', I2)

Check_Runge = abs(I1 - I2) / 15

if Check_Runge < e:
    print('Интеграл посчитан верно, точность составила:', Check_Runge, ', что выше, чем заданная точность', e)
else:
    print('Интеграл посчитан неверно, точность составила:', Check_Runge, ', что ниже, чем заданная точность', e)
