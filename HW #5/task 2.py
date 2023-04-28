# Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
import random

def Function(numbers, numbers2):
    counter = 0
    for i in numbers:
        counter += 1
        if i > numbers2[-1]:
            numbers2.append(i)
            print(numbers2)
            Function(numbers[counter:], numbers2)
    numbers2.pop()

numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
for i in range(len(numbers)):
    numbers2 = []
    numbers2.append(numbers.pop(0)) 
    Function(numbers, numbers2)
