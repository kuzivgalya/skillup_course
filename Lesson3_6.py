#1. Создать ф-цию которая будет возвращать группу детей в качестве списка из словарей
#2. Создать ф-цию которая будет возвращать группу детей в качестве списка из классов


from pprint import pprint

def task_1(amount_of_kids: int) -> list:
    """Returns list of dictionaries"""

    group_of_kids = []

    for i in range(amount_of_kids):
        kid = {}
        print('Kid ', i+1, ':')
        kid["name"] = input('Enter name: ')
        kid["surname"] = input('Enter surname: ')
        kid["age"] = input('Enter age: ')
        group_of_kids.append(kid)

    return group_of_kids

class Person:
#    pass
    def print_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}")
#   def __init__(self, name, surname, age):
#       self.name = name
#       self.surname = surname
#       self.age = age

def task_2(amount_of_kids: int) -> list:
    """Returns list of classes"""

    group_of_kids = []

    for i in range(amount_of_kids):
        kid = Person()
        print('Kid ', i+1, ':')
        kid.name = input('Enter name: ')
        kid.surname = input('Enter surname: ')
        kid.age = input('Enter age: ')
        group_of_kids.append(kid)

    return group_of_kids


#Get results
#==========================================
task_1_result = task_1(amount_of_kids=3)
task_2_result = task_2(amount_of_kids=3)


#Print results
#==========================================
print('Task 1:')
pprint(task_1_result)
print('Task 2:')
for element in task_2_result:
    element.print_info()



