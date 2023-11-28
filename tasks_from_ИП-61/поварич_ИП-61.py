#работа на оценку
#exercise 1
while True:
  def plus(a, b):
      return a+ b
  def minus(a, b):
      return a- b
  def umnogit(a, b):
      return a* b
  def delit(a, b):
      return a/ b
  while True:
      try:
          a = int(input('enter the first number: '))
          break
      except ValueError:
          print('enter a number!!')

  while True:
      try:
          b = int(input('enter the second number: '))
          break
      except ValueError:
          print('enter a number!!')
  while True:
      try:
          def1 = int(input('введите действие(1 - плюс, 2 - минус, 3 - умножить, 4 - разделить): '))
          break
      except ValueError:
          print('enter a number!!')

  if def1 == 1:
      print(plus(a, b))
  elif def1 == 2:
      print(minus(a, b))
  elif def1 == 3:
      print(umnogit(a, b))
  elif def1 == 4:
      try:
          print(delit(a, b))
      except ZeroDivisionError:
          print('на ноль делить нельзя!!')

  while True:
      try:
          bye = str(input('enter "exit" if you want to leave, else, enter "no"'))
          break
      except ValueError:
          print('enter the answer!!')
  if bye == exit:
      break
  elif bye == no:
      continue

#exercise2
def delete(brends):
    brends = list(brends)
    print(brends)
    word = str(input('какой бренд вы хотите удалить'))
    ind = brends.index(word)
    brends.pop(ind)
    brends = tuple(brends)
    print(brends)
def add(brends):
    brends = list(brends)
    print(brends)
    word = str(input('какой бренд вы хотите добавить'))
    brends.append(word)
    brends = tuple(brends)
    print(brends)
def change(brends):
    brends = list(brends)
    print(brends)
    word = str(input('какой бренд вы хотите изменить'))
    new_brend = str(input('на что вы хотите изменить'))
    ind = brends.index(word)
    brends[ind] = new_brend
    brends = tuple(brends)
    print(brends)
brends = ('apple', 'xiaomi', 'samsung', 'redmi', 'nike')
deff = int(input('что вы хотите сделать(1 - удалить, 2 - добавить, 3 - изменить'))
if deff == 1:
    delete(brends)
elif deff == 2:
    add(brends)
elif deff == 3:
    change(brends)
#exercise3
from random import randint
weight = int(input('enter weight of your array: '))
leight = int(input('enter leight of your array: '))
def random_array(weight,leight):
    a = []
    for i in range (weight):
        new_row = []
        for j in range(leight):
            new_row.append(randint(0, 9))
        a.append(new_row)
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
print(random_array(weight, leight))

#exercise 4
def delete(names):
    print(names)
    del_name = str(input('кого вы хотите удалить'))
    names.pop(del_name)
    print(names)
def change(names):
    print(names)
    change_name = str(input('у какого человека вы хотите изменить дату'))
    change_name1 = str(input('на какую дату вы хотите изменить'))
    names[change_name] = change_name1
    print(names)
def add1(names):
    print(names)
    add_name = str(input('введите имя человека'))
    add_data = int(input('какая дата рождения у человека'))
    names[add_name] = add_data
    print(names)

names = {'bob': 2000, 'sasha': 2003, 'jane': 1996, 'danil': 2007}
deff = int(input('что ты хочешь сделать(1 - удалить, 2 - изменить, 3 - добавить)'))
if deff == 1:
    delete(names)
elif deff == 2:
    change(names)
elif deff == 3:
    add1(names)

