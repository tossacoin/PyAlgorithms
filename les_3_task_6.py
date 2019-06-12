#В одномерном массиве найти сумму элементов,
#находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.


import random

#генерация массива

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
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

print ("Максимальное значение: ", max_num, ", Позиция в массиве: ",max_ind, "\nМинимальное значение: ", min_num, ", Позиция в массиве: ",min_ind )

i=min_ind+1
num_sum = 0
while i< max_ind:
    num_sum +=array[i]
    i+=1
print("Сумма чисел между максимальным и минимальным значением в массиве: ", num_sum)