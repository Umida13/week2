'''
 list comprehension 
dict comprehension
set comprehension
'''

# from binascii import a2b_hex
# from itertools import count
# from xxlimited import new


# new_list = list()

# for i in ["banana", "apple", "orange"]:
#     new_list.append(i)
# # print(new_list)
# new_list = [i for i in ["banana", "apple", "orange"]]
# print(new_list)


# for i in ['nursultan', 'erbol', 'isabar', 'umida', 'elina']:
#     new_list.append(i.capitalize())



# try:
#     num1 = int(input('enter number: '))
#     num2 = int(input('enter second number: '))
#     result = num1 + num2
# except ValueError:
#         print('Введите число!')
# else:
#         print(result)

# try:
#     num1 = int(input('enter number: '))
#     num2 = int(input('enter second number: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя !')
# else:
#     print(result)


    
#     new_list = [i.capitalize() for i in ['nursultan', 'erbol', 'isabar', 'umida', 'elina']]
# print(new_list)


# lists = list(range(1, 11))
# new_list = []
# for i in lists:
#     if i % 2 == 0:
#         new_list.append(i)

# new_list = [i for i in lists if i % 2 == 0]
# print(new_list)

# guests = ['nursultan', 'erbol', 'isabar', 'umida', 'elina']
# vip_guests = list()
# for name in guests:
#     if name == 'erbol':
#         vip_guests.append(name.capitalize())
# vip_guests = [i.capitalize() for i in guests if i == 'erbol']
# print(vip_guests)

# vip_guests = [i.capitalize() for i in guests if i.lower() == 'erbol']
# print(vip_guests)


# vip_guests = ['test' for i in guests if i.lower() == 'erbol']
# print(vip_guests)

# vip_guests = [len(i) for i in guests if i.lower() == 'erbol']
# print(vip_guests)




# mix = [1, 2, 3, 4, 5, 6, 1, 1, 1, 'test', 'test']
# new_mix = []
# for i in mix:
#     if i == 2:
#         new_mix.append(i)
#     else:
#         new_mix.append(2)
# print(new_mix)
# new_mix = [i if i == 2 else 2 for i in mix]
# # print(new_mix)
# print(len(new_mix) == len(mix))


# a = [1, 2]
# b = a.copy()

# print(a == b)
# print(a is b)


# from datetime import datetime
# from tracemalloc import start
# start = datetime.now()
# for i in range(1000):
#     new_list.append(i ** 2)
#     i ** 2
#     end = datetime.now()
#     print(end-start)

#     start = datetime.now()
#     new = [i ** 2 for i in range(1000)]
#     end = datetime.now()
#     print(end-start)



# dicts = dict.fromkeys(range(10), None)
# new_dicts = {k: v for k, v in dicts.items()}
# print(new_dicts)


# dicts = dict.fromkeys(range(10), None)
# new_dicts = {k for k in dicts.fromkeys(range(10)).keys()}
# print(new_dicts)


# new_dict = {}
# for k, v in {1: 2, 2: 2, 3: 3}.items():
#     if v % 2 == 0:
#         new_dict[k] = v
# print(new_dict)




# new_dicts = {k:None if k % 2 == 0 else 5 for k, v in {1: 1, 2: 2, 3: 3, 4: 4}.items()}
# print(new_dicts)




# lists = list(range(1, 11))
# odd = []
# even = []
# even = []
# even = [i if i % 2 == 0 else odd.append(i) for i in lists]
# print(even)



# lists = list(range(1, 11))
# lists.extend(list(range(1, 11)))
# print(lists)
# sets = {i for i in lists}
# print(sets)

# a = (i for i in range(11))
# print(a)   #<-- generator



# email_lists = []

# count = int(input("count: "))
# for i in range(count):
#     email = input("enter email: ")
#     if  "@" in email:
#         email_lists.append(email)
# else:
#     print("invalid email!!!")
  
#     email_lists = {i for i in email_lists}
#     print(email_lists)



# email_lists = []

# count = int(input("count: "))
# for i in range(count):
#     email = input("enter email: ")
#     if  "@" in email:
#         email_lists.append(email)
# else:
#     while True:
#         email = input("enter email: ")
#         if  "@" in email:
#             email_lists.append(email)
#             break
# email_lists = {i for i in email_lists}
#     print(email_lists)


# email_lists = []
# count = int(input("count: "))
# if count.isdigit():
#     i = 0
# while i < int(count):
#     email = input("enter email")
#     if email in email_lists:
#         print(f'Такой {email} писать заново')
#         continue
#     elif '@' in email and '.' in email:
#         email_lists.append(email)
#         i += 1
#     else:
#         print('invalid email!!!')





# for i in range(10):
#     for j  in range(10):
#         print(f'i={i},  j={j}')





# lists = [0, "test1", ["test2", "test3"]]
# for i in lists:
#     print(i)
#     answer = True if "__iter__" in dir(i) else False
#     if answer:
#         for j in i:
#             for c in j:
#                 print(c)


# lists = [["test2", "test3"], [1, 2, 3]]

# lists1 = [j for i in lists for j in i]
# print(lists1)



# dicts = {'nursultan': {'info': [1, 2, 3], "sex": 'M'}, "alia": {"info": [1, 2, 3], "sex": "F"}}
# new_dict = {k:v1 for k, v in dicts.items() for k1, v1 in v.items()}
# print(new_dict)
  
    
# try:
#     age = int(input('enter your age: '))
#     if age > 18:
# except ValueError:
#     print('Доступ запрещён')
# except:
#     print('Введён некорректный возраст ')
# else:
#     print('Спасибо ')
# finally:
#     print('До свидания!')



# try:
#     num1 = int(input('enter number: '))
#     num2 = int(input('enter second number: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('do not del to zero')
# except ValueError:
#     print('ener only numbers')


# nums = set([1, 2, 3, 3, 3, 3, 4])
# print(len(nums))

''' class work
'''

# try:
#   name = int(input('enter your age: '))
# except ValueError:
#     if name <= 0:
#         print('Ваш возраст должен быть больше 0')


# try:
#     num1 = int(input('enter number: '))
#     num2 = int(input('enter second number: '))
#     result = num1 +num2
# except:
#     print('num1' + 'num2')
# else:
#     print(result)




# inp1 = input()
# print(list(inp1))

# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'}
#     print(dict_['key5'])
# except KeyError:
#     print('Нет такого ключа!')
