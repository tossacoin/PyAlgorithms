#Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

ent_num = int(input("Введите число предприятий:"))
i=0
total_sum_rev=0
companies = []
Company = namedtuple('Company','name q1 q2 q3 q4 y')
while i<ent_num:
    curname= input(f"Введите название компании № {i+1}: ")
    j=0
    cur_rev = []
    while j<4:
        cur_rev.append(int(input(f"Введите прибыль за квартал № {j + 1}: ")))
        j+=1
    cur_sum_rev = sum(cur_rev)
    total_sum_rev += cur_sum_rev
    company_data = Company(curname,cur_rev[0], cur_rev[1], cur_rev[2], cur_rev[3],cur_sum_rev)
    companies.append(company_data)
    i+=1
avg_sum_rev = total_sum_rev / ent_num
print ("Средняя прибыль предприятий за год равна ", avg_sum_rev)

print ("Предприятия с прибылью выше среднего:")
for cur_comp in companies:
    if cur_comp.y > avg_sum_rev:
        print(cur_comp.name, " - прибыль за год ", cur_comp.y)

print ("Предприятия с прибылью ниже среднего:")
for cur_comp in companies:
    if cur_comp.y < avg_sum_rev:
        print(cur_comp.name, " - прибыль за год ", cur_comp.y)
