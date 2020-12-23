# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
# Задание 2
# Напишите функцию для нахождения минимума в списке целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых. 
# Список передаётся в качестве параметра. 
# Полученный результат возвращается из функции.
# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число. 
# Из функции нужно вернуть количество удаленных элементов.
# Задание 5
# Напишите функцию, которая получает два списка в качестве параметра и 
# возвращает список, содержащий элементы обоих списков.
# Задание 6
# Напишите функцию, высчитывающую степень каждого элемента списка целых. 
# Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра. 
# Функция возвращает новый список, содержащий полученные результаты.



def product_of_elements(list_of_int):    #product of elements in list
    prod = 1
    for element in list_of_int:
        prod *= element

    return prod


def min_element(list_of_int):    #minimum element of list
    return min(list_of_int)


def prime_numbers(list_of_int):    #amount of prime numbers in list
    counter = 0
    for element in list_of_int:
        if element > 1:
            for i in range(2, element):
                if element % i == 0:
                    break
            else:
                counter +=1

    return counter


def remove_num(list_of_int, num):    #amount of removed elements from list
    counter = 0
    for element in list_of_int:
        if element == num:
            list_of_int.remove(num)
            counter += 1

    return counter


def union_lists(list_1, list_2):    #concatenated list
    new_list = list_1 + list_2
    return new_list


def list_of_exp(list_of_int, k):    #list of exponentiations
    new_list = []
    for element in list_of_int:
        new_list.append(element**k)

    return new_list


a = [1, 3, 7, 5, 12, 16, 5]
b = [2, 1, 3, 2, 4, 5]

print('Product of elements in list:', product_of_elements(a))
print('Minimum element of list:', min_element(a))
print('Amount of prime numbers in list:', prime_numbers(a))
print('Amount of removed elements from list:', remove_num(a, 5))
print('Concatenated list:', union_lists(a, b))
print('List of exponentiations:', list_of_exp(b, 2))