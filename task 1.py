# Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели.

number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели неверное число! Попробуйте еще раз ;)')
elif number > 5:
    print('Ура! Этот день выходной!')
else:
    print('Увы, это рабочий день!')