#8. Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.

def count_digit(curnum, dig):

    k=0;
#    curnum = num;
#    i = 1;
    if curnum ==0 and dig = 0:
        k=1;
    while curnum!=0:
        temp = round(curnum % (10));
        if temp == dig:
           k=k+1;
        curnum = (curnum - (curnum % 10))/10;
 #       i = i + 1;

    return k;


num = int(input("Сколько чисел хотите ввести? "));
dig = int(input("Какую цифру будем искать? "));

i=0;
k=0;

while i<num:
    curnum = int(input("Введите число:"));
    k = k + count_digit(curnum, dig);
    i=i+1;
print("Цифра встретилась ", k, "раз.");
