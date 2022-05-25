''' dict - структура данных, измен, итер, не индекс, не упорядоч, хранит данные ввиде ключа значение
ключа - не изменяемый тип данных, уникальный и неизмен. тип  
значение - любой
'''




# test = dict()
# test1 = {}
# test2 = dict(a=1, b=2, c=3)
# test3 = dict.fromkeys(['a', 'b', 'c'],)
# print(test)
# print(test1)
# print(test2)
# print(test3)


# test = {'a':1, 'b':2, 'c':3}
# # print(*test)
# print(*test.values)
# test = {True: 1, 1:1}
# print(test)


# test = {[1]: False, {1}: 2, {3:3}:3}
# print(test)

# d = dict.fromkeys(range(1,10), "test1")
# # print(d)
# d[3] = "zmeika PEPa"
# print(d)
# print(d[3])



# for i in {'a': 1, 'b': 2, "c": 3, 'python19': [1,]}.keys():
#     print(i)


# print(dir(dict()))

# print(True if "__iter__" in dir(dict()) else False)
# print(True if "__iter__" in dir(list()) else False)
# print(True if "__iter__" in dir(tuple()) else False)
# print(True if "__iter__" in dir(str()) else False)

# b = "tet1"
# dicts = {"a": 1, b: 22, "c": 21}
# for i in (dicts.values()):
#     print(i)

# print(True if "__iter__" in dir(dicts.values()) else False)


# for i in dicts.keys():
#     print(i)

# for k in (dicts.items()):
#      print(k, "", v)
#      print(k([1]))
    #  print(*k)

# test = (1, 2, 3)
# print(*test)


# a,b = (1, 2)
# print(a, b)  <-- unpakking


# test = {"a": 1, "b": 2, "c": 3}
# print(*test.values())

# test = {"a": 1, "b": 2, "c": 3}

# a = list(test.values())
# a.append("test")
# print(a)
# b = {"a": a}
# print(b)
# print(a[:2])


# from copy import deepcopy

# lists = [1, 2, [1, 2, 3]]
# print(lists)
# lists2 = deepcopy(lists)
# lists2[-1][0] = "test"
# print(lists)




# dicts = {1: 1, 2: 2, 3: 3}
# print(dicts[3])

# print(dicts.get(4))
# a = dicts.get(4, 12) 
# dicts[4] = a
# print(dicts)



# dicts = {1: 1, 2: 2, 3: 3}
# print(dicts[3])

# a = dicts.get(4, None) 
# if a == None:
#     dicts[4] = a
# else:
#         print(a)




# dicts = {1: 1, 2: 2, 3: 3}
# a = dicts.setdefault(4, "test")
# print(a)
# print(dicts)

# dicts2 = dict.fromkeys(range(4, 10), "test1")
# dicts2 = test.fromkeys(range(4, 10), "test1")
# dicts2 = {}.fromkeys(range(4, 10), "test1")
# dicts.update(dicts2)

# "".join

# print(dicts)

# data ={"id: 1": {"name": None, "last_name": None, "age": None, "info": []}}
# data["id: 1"] = {"name": "Nursultan"}

# a = dict.fromkeys(range(30), None)
# for i in a:
#     a[i] = {"name": "Nursultan", "age": 25, "info": [123]}
#     print(a)
# a[2] = {'name': "daria", "age": 23, "info": {"desc": "test"}}
# a[2]["info"] = ["dog", "cat"]
# print(a[2])
''' 
id name  last_name
0  kalya test
1  daria test1
2  daria test2
'''




# test = {'name': "daria", "age": 23, "info": {"desc": "test"}}
# if 'info' in test:
#     print(test['info'])
# else:
#     print(test.setdefault('info', {'test1': 4}))
# print(test)





# num1 = int(input("enter number: "))
# num2 = int(input("enter second number: "))
# operator = input("enter operator: ")
# dicts = {'+': num1 + num2, '-': num1 - num2, '/': num1 / num2, '*': num1 * num2}
# print(dicts[operator] if dicts.get(operator) else 'error')


# while True:
#     num1 = int(input("enter number: "))
#     num2 = int(input("enter second number: "))
#     operator = input("enter operator: ")
#     if not operator:
#         break 
#     dicts = {'+': num1 + num2, '-': num1 - num2, '/': num1 / num2, '*': num1 * num2}
#     print(dicts[operator] if dicts.get(operator) else 'error')





# EXTRA TASK
# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# if inp2 == 1:
#     a[0].add(inp1)
#     a[1].add('defolt value')
#     a[2].add('defolt value')
# elif inp2 == 2:
#     a[0].add('defolt value')
#     a[1].add(inp1)
#     a[2].add('defolt value')
# elif inp2 == 2:
#     a[0].add('defolt value')
#     a[1].add('defolt value')
#     a[2].add(inp1)
# else: 
#     a[0].add('defolt value')
#     a[1].add('defolt value')
#     a[2].add('defolt value')


# for i in range(len(a)):
#     if i == inp2-1:
#         a[i].add(inp1)
# else:
#         a[i].add('default value')
# print(a)


# set1 = {i for i in range(0, 10, 2)}
# set2 = {i for i in range(1, 10, 2)}
# if set1.intersection(set2):
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')





# dicts = {1: 'a', 2: 'b', 3: 'c'}
# dicts1 = {}
# for k, v in dicts.items():
#   dicts1.update({v: k})
#   print(dicts1)

# university ={'программирование': 250, 'экономика': 320, 'медицина': 500}
# university['программирование'] = 150,
# # print(university)
# university['лингвистика'] = 110
# # print(university)
# print(university.pop('медицина'))
# print(sum(list(university.values())))



# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k, v in a.items():
#     if v % 2 ==0:
#         b[k] = 2
#     else:
#         b[k] = v

# print(b)      



# Дан словарь, удалите из него все элементы с пустыми значениями.

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = a.copy()
# for i in b:
#     if b[i] == None:
#         a.pop(i)
# print(a)



# Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение 
# которых будет чётным (специальным методом) и распечатайте результат.
# если меняем словарь, создаем копию!
# Ввод:

a = {'apple': 2, 'orange': 5, 'banana': 10} 
b = a.copy()

for i in b:
    if b[i] % 2 ==0:






#         Напишите код, который создает словарь следующим образом, вам дана строка, например:

# 
# нужно создать новый словарь, ключами которого будут буквы строки, а значениями числа,
#  соответствующие количеству повторений данной буквы в строке.
 
# dict_ = {"p":1, "y":1, "t":2, "h":1, "o":1, "n":1, "i":1, "s":1} 

# string = "pythonist"
# dict_ = {}
# for i in string:
#     dict_.update({i:string.count(i)})
# print(dict_)


# Задание 3
# Создайте список используя

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# и запишите в новый список int_list

# только четные числа, которые больше нуля. Нужно использовать comprehension.

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [num for num in list_ if num % 2 == 0 and num > 0]
# print(int_list)

# Задание 8
# Создайте список из 10 произвольных имён list_name.

# Затем пройдитесь по данному списку и если длина имени меньше или равна 4 буквам 
# создайте список new_list имя на shorter, а если больше на longer.
# Пример:

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# Вывод в терминале:

# ['shorter', 'shorter', 'longer', 'longer', 'shorter', 'longer', 'shorter', 'longer', 'longer', 'shorter'] 
# Нужно использовать comprehension.

# list_name = ['shaun', 'jhon', 'erika', 'natali', 'leo']
# new_list = ['shorter' if len(name) <= 4 else 'longer' for name in list_name]
# print(new_list)



