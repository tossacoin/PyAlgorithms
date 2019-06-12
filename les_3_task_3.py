#3В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

#генерация массива

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

#поиск максимального и минимального
max_num = array[0]
max_ind = 0
min_num = array[0]
min_ind = 0
i=0
while i< len(array):
    if array[i]< min_num:
        min_num = array[i]
        min_ind = i
 #       print (array[i], min_num, min_ind)

    if array[i]> max_num:
        max_num = array[i]
        max_ind = i
 #       print (array[i], max_num, max_ind)
    i+=1
#смена позиций максимального и минимального
print ("Максимальное значение: ", max_num, ", Позиция в массиве: ",max_ind, "\nМинимальное значение: ", min_num, ", Позиция в массиве: ",min_ind )
array[min_ind] = max_num
array[max_ind] = min_num

print("Новый массив:\n", array)