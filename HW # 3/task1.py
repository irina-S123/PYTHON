# Создайте список. Запишите в него N первых
# элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1, 6):
    print(i, fib(i))