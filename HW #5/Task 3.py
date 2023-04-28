# Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]
import random
numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
result = set(numbers)
print(list(result))
print(f"{len(numbers) - len(result)} повторяющихся элемента")