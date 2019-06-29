#Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#Алгоритм с использованием решета Эратосфена


import cProfile
import timeit

def find_prime(k):
    n = 2000

    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

#    print(sieve)
    res = [i for i in sieve if i != 0]
#    print (len(res))
    return(res[k-1])

k = int(input("Введите номер простого числа не более 300: "))
print(find_prime(k))

#cProfile.run('find_prime(300)')


#k=40, 100 loops, best of 5: 696 usec per loop

#k = 20, 100 loops, best of 5: 697 usec per loop
#k = 20, 1000 loops, best of 5: 716 usec per loop
#k = 20, 10000 loops, best of 5: 737 usec per loop

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#        1    0.001    0.001    0.002    0.002 les_4_task_2_sieve.py:11(find_prime)
#        1    0.000    0.000    0.000    0.000 les_4_task_2_sieve.py:14(<listcomp>)
#        1    0.000    0.000    0.000    0.000 les_4_task_2_sieve.py:25(<listcomp>)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Данный алгоритм зависит от заранее заданно длины решета и не гибок
#Время выполнения данного алгоритма не изменилось при увеличении параметра k
# и осталось практически константным за счет того,
# что просеивание осуществляется по всему решету
#Сложность алгоритма - константная

#при увеличении количества прогонов время не изменилось существенно

