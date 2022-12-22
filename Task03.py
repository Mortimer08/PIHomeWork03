# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from decimal import Decimal


def random_list():
    custom_list = []
    for _ in range(6):
        index = random.randint(0, 3)
        custom_list.append(round(random.uniform(0, 10), index))
    return custom_list


def fractional(number):
    str_number = str(number)
    fract_part_start = str_number.find('.')+1
    fract_part_lenght = len(str_number)
    return Decimal('0.' + str_number[fract_part_start:fract_part_lenght])


my_list = random_list()

print('Список:')
print(my_list)

max_fractional = fractional(my_list[0])

for i in my_list:
    item_fractional = fractional(i)
    if item_fractional != 0 and item_fractional > max_fractional:
        max_fractional = item_fractional

min_fractional = max_fractional
for i in my_list:
    item_fractional = fractional(i)
    if item_fractional != 0 and item_fractional < min_fractional:
        min_fractional = item_fractional

max_min_difference = max_fractional - min_fractional

print(f'Разница между максимальной и минимальными дробными частыми равна {max_min_difference}')
