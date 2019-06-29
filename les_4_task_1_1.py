#PЗадача 6 (Урок 3)
#Варивант 1 - Исходный
#В одномерном массиве найти сумму элементов,
#находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.


import random
import cProfile



def sum_diff(SIZE):
    # генерация массива
    MIN_ITEM = 0
    MAX_ITEM = 1000
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

    if min_ind<max_ind:
        i=min_ind+1
        num_sum = 0
        while i< max_ind:
            num_sum +=array[i]
            i+=1
    else:
        i=max_ind+1
        num_sum = 0
        while i< min_ind:
            num_sum +=array[i]
            i+=1
    print("Сумма чисел между максимальным и минимальным значением в массиве: ", num_sum)
    return num_sum

SIZE = 100
num_sum = sum_diff(SIZE)

#sum_diff(100), n = 100
#100 loops, best of 5: 2.23 msec per loop

#sum_diff(1000), n = 100
#100 loops, best of 5: 8.79 msec per loop


#sum_diff(10000), n = 100
#100 loops, best of 5: 63.7 msec per loop


#cProfile.run('sum_diff(10000)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.053    0.053 <string>:1(<module>)
#        1    0.007    0.007    0.053    0.053 les_4_task_1_1.py:13(sum_diff)
#        1    0.004    0.004    0.037    0.037 les_4_task_1_1.py:17(<listcomp>)
#    10000    0.014    0.000    0.027    0.000 random.py:174(randrange)
#    10000    0.005    0.000    0.032    0.000 random.py:218(randint)
#    10000    0.010    0.000    0.014    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
#    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#        3    0.008    0.003    0.008    0.003 {built-in method builtins.print}
#    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    10239    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
