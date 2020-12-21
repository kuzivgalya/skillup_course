#Задание 1
#Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.
#Задание 2
#Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.
#Задание 3
#Есть три кортежа целых чисел необходимо найти эле- менты, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции.

import random

length_1=int(input('Enter the length of the tuple_1: '))
length_2=int(input('Enter the length of the tuple_2: '))
length_3=int(input('Enter the length of the tuple_3: '))

x_1=random.sample(range(1,10),length_1)
x_2=random.sample(range(1,10),length_2)
x_3=random.sample(range(1,10),length_3)

tuple_1=tuple(x_1)
tuple_2=tuple(x_2)
tuple_3=tuple(x_3)

print(tuple_1)
print(tuple_2)
print(tuple_3)
print()


print('Task 1')

tuple_1_set=set(tuple_1)
tuple_2_set=set(tuple_2)
tuple_3_set=set(tuple_3)
common_elements=tuple_1_set&tuple_2_set&tuple_3_set
if len(common_elements)==0:
    print("There aren't common elements")
else:
    print('Common elements:', common_elements)
print()


print('Task 2')

tuple_1_unique_elements=tuple_1_set-tuple_2_set-tuple_3_set
if len(tuple_1_unique_elements)==0:
    print('There are no unique element in tuple 1')
else:
    print('Unique elements for tuple 1:', tuple_1_unique_elements)

tuple_2_unique_elements=tuple_2_set-tuple_1_set-tuple_3_set
if len(tuple_2_unique_elements)==0:
    print('There are no unique element in tuple 2')
else:
    print('Unique elements for tuple 2:', tuple_2_unique_elements)

tuple_3_unique_elements=tuple_3_set-tuple_2_set-tuple_1_set
if len(tuple_3_unique_elements)==0:
    print('There are no unique element in tuple 3')
else:
    print('Unique elements for tuple 3:', tuple_3_unique_elements)

print()


print('Task 3')

for i in range(min(length_1,length_2,length_3)):
    if tuple_1[i]==tuple_2[i]==tuple_3[i]:
        print('On ', i ,'th position there is common element - ', tuple_1[i])
    else:
        print('Elements on ', i, 'th position are not equal')
