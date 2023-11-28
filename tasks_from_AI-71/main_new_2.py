from random import *
my_lst = [randint(0, 50) for i in range(20)]
my_lst.sort()
print(my_lst)
num = int(input('введите число: '))

def insert_k(lst, k):
    n = binary_search(my_lst, num)
    for i in range(len(lst)-1):
        if k == lst[n]:
            lst.insert(n, k)
            break
        elif k < lst[i] and k > lst[i-1]:
                lst.insert(i, k)
                break
        else:
            continue
    return lst
def binary_search(lst, k):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low+high) // 2
        if lst[mid] == k:
            return mid
        elif lst[mid] > k:
            high = mid - 1
        else:
            low = mid +1
    return -1

print(insert_k(my_lst, num))
