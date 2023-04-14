# Напишите программу, которая на вход
# принимает число (N), а на выходе показывает все чётные
# числа от 1 до N. python

n = int(input("Введите любое положительное число: "))

counter = 1
while counter <= n:
   print(2*counter)
   counter = counter + 1