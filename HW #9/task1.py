# Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.
import numpy as np
import random

numbers = [random.randint(1, 10) for i in range(10)]

print(numbers)
print(f'Уникальных элементов - {len(np.unique(numbers))}')