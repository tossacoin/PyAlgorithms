# Задача 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

input_str = input("Введите трехзначное целочисленное число: ")

if len(input_str) == 3:
    if input_str.isdigit():
        a = int(input_str) // 100
        b = int(input_str) % 100
        b = b // 10
        c = int(input_str) % 10
        x = a + b + c
        y = a * b * c
        print("Сумма цифр числа = ", x)
        print("Произведение цифр числа = ", y)

    else:
        print("Введенное значение не является числом")
else:
    print("Длина введенного значения не равна 3")