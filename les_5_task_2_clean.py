#Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

#определение ключа по значению словаря
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return str(k)


#функция сложения. возвращает список символов в 16сс
def find_sum(num1, num2):
    d1 = {str(a): a for a in range(10)}
    d2 = {chr(ord("a") + a - 10): a for a in range(10, 16)}
    d1.update(d2)


    k = max(len(num1), len(num2))
    num1.reverse()
    num2.reverse()
    val_sum = []

    i=0
    buf = 0
    while i<k:

        if ((len(num1)-1)>=i ):
            val1 = d1[str(num1[i])]
        else:
            val1 = 0
        if ((len(num2)-1)>=i ):
            val2 = d1[str(num2[i])]
        else:
            val2 = 0
        if (val1 + val2 + buf) <=9:
            val_sum.append( get_key(d1,(val1 + val2 + buf)))
            buf = 0
        else:
            val_sum.append (get_key(d1,(val1 + val2 + buf)%16))
            buf = (val1 + val2 + buf)//16

        i+=1

    if buf != 0:
        val_sum.append (get_key(d1,buf))

    val_sum.reverse()
    return val_sum


#-------------------ввод чисел:
num1= list(input("Введите первое число в 16ричной системе счисления:").lower())
num2= list(input("Введите второе число в 16ричной системе счисления:").lower())
#формирование словаря
d1 = {str(a): a for a in range(10)}
d2 = {chr(ord("a") + a -10): a for a in range(10,16)}
d1.update(d2)
print (d1)
#-------------------сложение:
val_sum = find_sum(num1, num2)

#преобразование списка в строку для вывода результатов
num_sum = ''
i = 0
while i < len(val_sum):
    num_sum += str(val_sum[i])
    i += 1
print ("Результат сложения", num_sum)


#--------------------умножение
val_mult = []

k = len(num1)
n = len(num2)
i=0
buf = 0

while i<k:
    #временное значение для результатов умножения на
    val_temp = []
    val1 = d1[str(num1[i])]
    j=0
    while j<n:
        val2 = d1[str(num2[j])]
        if (val1 * val2 + buf) <=9:
            val_temp.append( get_key(d1,(val1 * val2 + buf)))
            buf = 0
        else:
            val_temp.append (get_key(d1,(val1 * val2 + buf)%16))
            buf = (val1 * val2 + buf)//16

        j+=1

    if buf != 0:
        val_temp.append(get_key(d1, buf))
        buf=0
#"переворачиваем" временное значение для сложения
    val_temp.reverse()

#выравниваем разряд
    if i!=0:
        kk=0
        while kk < i:
            val_temp.append('0')
            kk+=1
#складываем с результатами умножения предыдущих разрядов
    if len(val_mult)==0:
        val_mult = val_temp
    else:
        val_mult = find_sum(val_mult, val_temp)

    i+=1

#преобразование списка в строку для вывода результатов
num_mult = ''
q = 0
while q < len(val_mult):
    num_mult += str(val_mult[q])
    q += 1

print ("Результат умножения: ",num_mult)