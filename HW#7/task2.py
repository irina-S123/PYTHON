# Создайте декоратор, повторяющий функцию заданное количество раз.
import random


def repeater(iter_num):
    def our_repeater(func):
        def decorator(*args):
            for i in range(0, iter_num):
                func(*args)
        return decorator
    return our_repeater

@repeater(int(input("Задайте число повторений: ")))
def print_random():
    print(random.randint(1, 10))

print_random()