#7В одномерном массиве целых чисел определить два наименьших элемента.
#Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

#генерация массива

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

#поиск максимального и минимального
min_num1 = array[0]
min_ind1 = 0
i=min_ind1
while i< len(array):
    if array[i]< min_num1:
        min_num1 = array[i]
        min_ind1 = i
 #       print (array[i], min_num1, min_ind1)
    i+=1

print ("Минимальное значение 1: ", min_num1, ", Позиция в массиве: ",min_ind1 )

if min_ind1!=0:
    min_num2 = array[0]
    min_ind2 = 0
else:
    min_num2 = array[1]
    min_ind2 = 1

i=min_ind2
#print(i, min_ind1, min_ind2)
while i< len(array):
    if i != min_ind1:
#        print("Indexies: ", min_ind1, min_ind2, i )
        if array[i]< min_num2:
            min_num2 = array[i]
            min_ind2= i
#            print (array[i], min_num2, min_ind2)
    i+=1


print ("Минимальное значение 2: ", min_num2, ", Позиция в массиве: ",min_ind2 )
