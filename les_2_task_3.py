# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

z = input("Введите целое натуральное число: ");
if int(z):
    len_z = len(z);
    i = 1 ;
    newnum = 0;
    while i <= len_z:
        if i==1:
            temp =  int(z) % (10 ** i)
        else:
            temp = (int(z) % (10 ** i) - int(z) % (10 ** (i-1))) * (10 ** -(i-1));
        newnum += temp * (10 ** (len_z - i));
        i = i + 1;
    print("Обратное по порядку цифр число = ", int(newnum));

else:
    print("Введеное значение не является целым натуральным числом");
