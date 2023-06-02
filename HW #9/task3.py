# Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.
import numpy as np
import random

size = (random.randint(2, 10), random.randint(2, 10))

numbers = np.random.randint(1, 100, size)

print(numbers)
print(np.unravel_index(np.argmax(numbers), numbers.shape))
print(np.unravel_index(np.argmin(numbers), numbers.shape))
print(np.diagonal(numbers))