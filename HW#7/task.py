# Создайте пользовательский аналог метода map()
def my_map(func, numbers):
    return (func(el) for el in numbers)


numbers = [1, 14, 6, 10, 3, 2, 5]

print(list(my_map(lambda x: x * 2, numbers)))