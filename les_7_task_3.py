#3 Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

def find_mediana(arr):
    n=len(arr)
    more = []
    less = []

    i=0
    while i< n:
        j=0
        more.append(0)
        less.append(0)
        while j< n:
            if i!=j:
                if arr[i] > arr[j]:
                    more[i] +=1
                else:
                    less[i] +=1
            j+=1
        i+=1

    i=0

    mediana = -999
    mediana_ind = -999

    print (more, "\n", less)
    while i<n:
        if more[i] == (n-1)/2 and more[i]== less[i] :
            mediana_ind = i
            mediana = arr[i]
            break
        i+=1
    print (mediana, mediana_ind)
    return mediana


n=21
arr = [round(random.uniform(0,100)) for x in range(n)]

print("Исходный массив:\n", arr)
mediana= find_mediana(arr)
print ("Элемент со значением ", mediana, " является медианой")