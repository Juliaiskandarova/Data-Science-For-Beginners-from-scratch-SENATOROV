"""Lesson 1 Module."""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.special as scs
import seaborn as sns

# # 24.08
# Вводный урок, начали разбирать комбинаторику:
#
# Перестановки, Число сочетаний

# # Lesson 2 maths test
#  Ряд Тейлора - это разложение функции в полином(многочлен).
#
#  Декартова система координат - прямоугальная система координа.т (ox, oy).
#
#  import math as m
#
#  cosx = 1 - x**n/m.factorial(n) + x**n+=2/m.factorial(n+=2) - .....
#
#  Четные функции это функции, симметричные относительно оси oy.
#
#  cosx = cos(-x).
#
#  Степенная функция это y = x**n.

# # Lesson 3. ТеорВер и Матстат. Начало
#
# **три вида событий:**
#
# невозможное
#
# достоверное
#
# случайное
#
# События называют несовместными, если в одном и том же испытании появление одного из событий исключает появление других событий.
#
# примером несовместных событий  является пара противоположных событий.
# не B5^ = B1 + B2 + B3 + B4 + B6
#
# Несовместные события образуют полную группу, если в результате отдельно взятого испытания обязательно появится одно и только одно из этих событий.
#
# Элементарное событие это то событие, которое нельзя разложить на другие.
#
# События называются совместными, если в отдельно взятом испытании появление одного из них не исключает появление другого.
#
# Сложение событий обозначает логическую связку ИЛИ,
# а умножения событий – логическую связку И.
#
# Суммой двух событий  и  называется событие  которое состоит в том, что наступит или событие , или событие , или оба события одновременно. В том случае, если события несовместны, последний вариант отпадает, то есть может наступить или событие  или событие .
#
# C1^3
# 1) если наверху единица всегда пишем нижнее,
#
# 2) если наверху число отличается на 1 от нижнего пишем всегда нижнее
#
# 3) когда сверху и снизу одинаковые числа пишем единицу
#

# Методы и атрибуты объекта
dir(str)

# +
# Сигнатура объекта
# str.lower?
# -

# # 17-10

x_: int = 4

o_: float = np.sqrt(x_)
o_

r_: float = np.cbrt(x_)
r_

w_: float = np.square(x_)
w_

np.abs(x_)  # |a| - module

np.sign(x_)  # везде где нужно
# перевести данные в двоичную систему
# применяем функцию sign

# ![images.png](attachment:images.png)

np.exp(x_)  # экспонента

np.power(2, x_)

np.log(x_)  # ln
np.log(10)  # lg
np.log2(10)

np.sin(np.pi * 1 / 4)

i_: float = np.around(2.667)
i_

# +
# через точку мы перемещаеимся на уроень ниже в директории
sc.special.factorial(5)

# (a + b) ^ n   формула Бинома
# -

# ![maxresdefault.jpg](attachment:maxresdefault.jpg)

plt.figure(figsize=(8, 6))
data = scs.comb(10, [1, 2, 3, 4, 5, 6, 8, 9])
sns.histplot(data, bins=len(data))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(axis="y", linestyle="--")
plt.show()

scs.perm([5, 6], [4, 3])  # размещения

# +
x__ = np.linspace(0, 5, 100)
y__ = np.exp(x__)

f1 = y__ + 2
f2 = 10 * x__
plt.plot(x__, f1)
plt.plot(x__, f2)
plt.show()
# -

# # Метод монтекарло это метод моделирования случайных величин

# +
# инициальзация генератора - воспроизведение эксперимента
np.random.seed(100)

data = np.arange(10)

np.random.choice(data, 10, replace=False)
# [7, 6, 1, 5, 4, 2, 0, 3, 9, 8]
# -

# дз расписать бином ньютона до второй степени (с 0 ) и записать коэффициенты в треугольник паскаля
#
# data cleaning
# книга визуализация
# питон это просто

# # 24-10

# Кода нажимаем кнопку stash все файлы под модификацией они добавляются во временный буфер обмена (небезопасно там держать файлы), незакоммиченные файлы никуда не пропадают а просто добавляются в ОЗУ

# Если кошка умерла вводим в терминал команды:
#
# git pull
#
# git add .
#
# git commit -m 'test'
#
# git push

# Issues создают пользователи которые сами не могут отдать пулл реквест (сообщить о проблеме, улучшении проекту), обязательно указываем номер issues пишем fixes #issues-number

# 29 ноя
#
# Изучали CDF и PDF
