# Определить, какое число в массиве встречается чаще всего.

def count_num(array, num):
    #функция подсчитывает количество вхождений заданного значения в массиве
    c = 0
    for _ in array:
        if _ == num:
            c+=1
    return c

#генерация исходного массива
import random
SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

#формирование массива уникальных значений:
uni_array = []
i=0

while i< len(array):
    flag = 0
    j=0
    while j < i:
        if array[i] == array[j]:
            flag=1
            break
        j+=1
    if flag ==0:
        uni_array.append(array[i])

    i+=1

print("Исходный массив:\n", array)
print("Массив уникальных значений: \n", uni_array)

#рассчет количества вхождений каждого числа в массив
count_array = []
for num in uni_array:
    count_array.append(count_num(array, num))

print ("Количество вхождений каждого числа в исходный массив: \n", count_array)

#поиск максимального
max_num = count_array[0]
max_pos = 0
i=0
while i<len(count_array):
    if(count_array [i]> max_num):
        max_num = count_array[i]
        max_pos = i
    i+=1

print ("Максимальное количество вхождений:", max_num, " у числа: ",uni_array[max_pos] )