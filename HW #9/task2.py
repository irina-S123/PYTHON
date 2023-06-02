# Создайте двумерный массив, размером 5х5. 
# Определите, есть ли в нём одинаковые строки.
import numpy as np
import random

size = (5,5)
numbers = np.random.randint(1, 3, size)
print(numbers)

answer = False

for i in range(5):
    for j in range(i, 5):
        if not (i == j) and not (False in (numbers[i, :] == numbers[j, :])):
           answer = True

if answer: print("Есть")
else: print("Нет")