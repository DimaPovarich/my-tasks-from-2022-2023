#на оцунку 4
#exercise 1
# from random import randint
# list1 = []
# list2 = []
# a = int(input('какой длинны будет первый список '))
# b = int(input('какой длинны будет второй список '))
# for i in range(0, a):
#     list1.append(randint(0, 10))
# for j in range(0, b):
#     list1.append(randint(0, 10))
#
# new_list = list1 + list2
# print(new_list)
#
# print('сортированный список', list(sorted(new_list)))
#
# uniq_numbers = list(set(new_list))
# print(uniq_numbers)
#
# print('наибольшее число: ', max(new_list))
# print('наименьшее число: ', min(new_list))

#exercise 2
# man1 = int(input('уровень продаж 1 менеджера: '))
# man2 = int(input('уровень продаж 2 менеджера: '))
# man3 = int(input('уровень продаж 3 менеджера: '))
#
# def zp(manager):
#     if manager < 500:
#         zp = 200 + (manager//100)*3
#         return zp
#     elif manager >= 500 and manager < 1000:
#         zp = 200 + (manager//100)*3
#         return zp
#     elif manager >= 1000:
#         zp = 200+(manager//100)*8
#         return zp
#
# zp_man1 = zp(man1)
# zp_man2 = zp(man2)
# zp_man3 = zp(man3)
#
#
# if zp_man1 > zp_man2 and zp_man1 > zp_man3:
#     zp_man1 += 200
# if zp_man2 > zp_man1 and zp_man2 > zp_man3:
#     zp_man2 += 200
# if zp_man3 > zp_man2 and zp_man3 > zp_man1:
#     zp_man3 += 200
# print('зп первого менеджера: ', zp_man1)
# print('зп второго менеджера: ', zp_man2)
# print('зп третьего менеджера: ', zp_man3)

#exercise 3
# def delete(brends):
#     print(brends)
#     del1 = str(input('какой бренд вы хотите удалить: '))
#     brends = list(brends)
#     del1_ind = brends.index(del1)
#     del brends[del1_ind]
#     print(tuple(brends))
#
# def add(brends):
#     print(brends)
#     add_brand = str(input('какой бренд вы хотите добавить: '))
#     brends = list(brends)
#     brends.append(add_brand)
#     print(tuple(brends))
# brends = ('samsung', 'xiaomi', 'apple', 'redmi')
# def1 = int(input('что вы хотите сделать(1 - удалить, 2 - добавить) '))
# if def1 == 1:
#     delete(brends)
# elif def1 == 2:
#     add(brends)

#exercise 4
# my_set = {'russia', 'japan', 'china', 'america'}
# def1 = int(input('что вы хотите сделать(1 - найти страну, 2 - удалить страну, 3 - записать новую страну) '))
# if def1 == 1:
#     find1 = str(input('какую страну вы хотите найти: '))
#     my_set = list(my_set)
#     if find1 in my_set:
#         print('страна', find1, 'найдена')
#         print('индекс страны: ', my_set.index())
#     else:
#         print('страна', find1, 'не найдена')
#     my_set = set(my_set)
# elif def1 == 2:
#     print(my_set)
#     del1 = str(input('какую страну вы хотите удалить: '))
#     my_set = list(my_set)
#     del1_ind = my_set.index(del1)
#     del my_set[del1_ind]
#     print(set(my_set))
#
# elif def1 == 3:
#     new_country = str(input('какую страну вы хотите добавить: '))
#     my_set = list(my_set)
#     my_set.append(new_country)
#     print(set(my_set))
#

#exercise 5
# names = {'bob': 2003, 'jone': 2010, 'karl': 2006, 'dima': 2014}
# def1 = int(input('что вы хотите сделать(1 - удалить, 2 - изменить, 3 - добавить): '))
# if def1 == 1:
#     print(names)
#     del1 = str(input('какое имя вы хотите удалить '))
#     names.pop(del1)
#     print(names)
# elif def1 == 2:
#     print(names)
#     change_name = str(input('у кого вы хотите изменить год рождения: '))
#     change_name1 = int(input('на какой год вы хотите изменить: '))
#     names[change_name] = change_name1
#     print(names)
# elif def1 == 3:
#     add_name = str(input('какого человека вы хотите добавить: '))
#     add_name1 = int(input('в каком году родился этот человек: '))
#     names[add_name] = add_name1
#     print(names)

#exercise 6

# import random
# lst = list(range(int(input('enter the range: '))))
# for i in range(len(lst)):
#     lst.insert(random.randint(0, 9), lst.pop(i))
# print(lst)