#1
#from math import pi
#d = int(input("Введите число для заданной точности числа Пи:\n"))
#print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

#2
#num = int(input("Введите число: "))
#i = 2  # первое простое число
#lst = []
#old = num
#while i <= num:
#    if num % i == 0:
#        lst.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
#print(f"Простые множители числа {old} приведены в списке: {lst}")


#3
#lst = list(map(int, input("Введите числа через пробел:\n").split()))
#print(f"Исходный список: {lst}")
#new_lst = []
#[new_lst.append(i) for i in lst if i not in new_lst]
#print(f"Список из неповторяющихся элементов: {new_lst}")

#4
#import random

#def write_file(st):
#    with open('file33.txt', 'w') as data:
#        data.write(st)
#def rnd():
#    return random.randint(0, 101)
#def create_mn(k):
#    lst = [rnd() for i in range(k+1)]
#    return lst
#def create_str(sp):
#    lst = sp[::-1]
#    wr = ''
#    if len(lst) < 1:
#        wr = 'x = 0'
#    else:
#        for i in range(len(lst)):
#            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                wr += f'{lst[i]}x^{len(lst)-i-1}'
#                if lst[i+1] != 0:
#                    wr += ' + '
#            elif i == len(lst) - 2 and lst[i] != 0:
#                wr += f'{lst[i]}x'
#                if lst[i+1] != 0:
#                    wr += ' + '
#            elif i == len(lst) - 1 and lst[i] != 0:
#                wr += f'{lst[i]} = 0'
#            elif i == len(lst) - 1 and lst[i] == 0:
#                wr += ' = 0'
#    return wr
#k = int(input("Введите натуральную степень k = "))
#koef = create_mn(k)
#write_file(create_str(koef))



#5
