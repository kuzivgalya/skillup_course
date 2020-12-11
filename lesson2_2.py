#1. Пользователь вводит 3 числа. В зависимости от выбора нужно найти сумму или произведение чисел.
#2. Пользователь вводит 3 числа. В зависимости от выбора нужно найти максимальное или минимальное значение.
#3. Пользователь вводит количество метров. В зависимости от выбора нужно конвертировать данные в километры или миллиметры.

#Со звездочкой:
#1. Добавить до каждого из заданий 3 варианта развитий событий (elif)

print("Task 1:")

number_1=float(input('Enter number_1: '))
number_2=float(input('Enter number_2: '))
number_3=float(input('Enter number_3: '))

print("Enter '1' to find the sum of numbers")
print("Enter '2' to find the product of numbers")
print("Enter '3' to find the fraction of 2 numbers")

choice_1=input()

if choice_1=='1':
    print("sum= ",number_1+number_2+number_3)
elif choice_1=='2':
    print("product= ",number_1*number_2*number_3)
else:
    print("fraction= ",number_1/number_2)


print("Task 2:")

number_01=float(input('Enter number_1: '))
number_02=float(input('Enter number_2: '))
number_03=float(input('Enter number_3: '))

print("Enter '1' to find the maximum of numbers")
print("Enter '2' to find the minimum of numbers")

choice_2=input()

if choice_2=='1':
    print("max= ",max(number_01,number_02,number_03))
else:
    print("min= ",min(number_01,number_02,number_03))


print("Task 3:")

m=float(input('Enter the length in meters: '))

print("Enter '1' to convert your value to kilometers")
print("Enter '2' to convert your value to millimeters")
print("Enter '3' convert your value to centimeters")

choice_3=input()

if choice_3=='1':
    print(m," meters = ",m/1000," kilometers")
elif choice_3=='2':
    print(m," meters = ",m*1000," millimeters")
else:
    print(m," meters = ",m*100," centimeters")

