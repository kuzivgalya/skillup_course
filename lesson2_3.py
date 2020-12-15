#Два списка целых заполняются случайными числами. Необходимо:
#■ Сформироватьтретийсписок,содержащийэлементы обоих списков;
#■ Сформироватьтретийсписок,содержащийэлементы обоих списков без повторений;
#■ Сформироватьтретийсписок,содержащийэлементы общие для двух списков;
#■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
#■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

import random
length_1=int(input('Enter the length of the list_1: '))
length_2=int(input('Enter the length of the list_2: '))
list_1=[]
for num in range(length_1):
    list_1.append(random.randint(1,10))
list_2=[]
for num in range(length_2):
    list_2.append(random.randint(1,10))
print("List_1 = ",list_1)
print("List_2 = ",list_2)
print()

print("Task 1")
list_3=list_1+list_2
print(list_3)
print()

print("Task 2")
list_4=[]
for num in list_3:
    if num not in list_4:
        list_4.append(num)
print(list_4)
print()

print("Task 3")
list_5=[]
for num in list_1:
    if num in list_2:
        list_5.append(num)
print(list_5)
print()  

print("Task 4")
list_1_unique_elements=[]
for num in list_1:
    if list_1.count(num)==1:
        list_1_unique_elements.append(num)
list_2_unique_elements=[]
for num in list_2:
    if list_2.count(num)==1:
        list_2_unique_elements.append(num)
list_6=list_1_unique_elements+list_2_unique_elements
print(list_6)
print()

print("Task 5")
list_1.sort()
list_2.sort()
list_7=[list_1[0],list_1[-1],list_2[0],list_2[-1]]
print(list_7)



