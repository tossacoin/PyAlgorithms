#Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#Классический алгоритм

import cProfile
import timeit

def find_prime(n):
    lst = []
    k=0
    i=2

    while k<n:
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            lst.append(i)
            k+=1
        i+=1
    print (lst[n-1])


n = int(input("Введите номер просторого числа n="))
print (find_prime(n))

#cProfile.run('find_prime(300)')

#python -m timeit -n 100 -s "import les_4_task_2_wo_sieve" "les_4_task_2_wo_sieve.find_prime(20)"
#n=40, 100 loops, best of 5: 579 usec per loop
#n=20, 100 loops, best of 5: 234 usec per loop
#n=20, 1000 loops, best of 5: 280 usec per loop
#n=20, 10000 loops, best of 5: 239 usec per loop

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#        1    0.020    0.020    0.020    0.020 les_4_task_2_wo_sieve.py:10(find_prime)
#        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      300    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Сложность алгоритма - Q(n) - время выполнения возрастает линейно при увеличении аргумента
#при увеличении количества прогонов время не изменилось существенно


