#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#from random import randint
#spisok = [randint(0,20) for i in range(randint(5,10))]
#sum=0
#for i in range(1,len(spisok),2):
#    sum += spisok[i]

#print(spisok)
#print(sum)


#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#from random import randint
#spisok = [randint(0,20) for i in range(randint(5,10))]
#print(spisok)
#multi=[]
#lenght = len(spisok)
#middle = lenght//2 + lenght%2
#for i in range(middle):
#    multi.append(spisok[i]* spisok[lenght-i-1])
#print(multi)



#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#import random
#def fract(num):
#    return round(num%1,2)

#spisok = [round(random.uniform(0,20),2) for i in range(random.randint(5,10))]
#print(spisok)
#spisok_fract = []
#for i in spisok:
#    if i%1!=0:
#        spisok_fract.append(fract(i))
#print(spisok_fract)
#max_num,min_num = spisok_fract[0],spisok_fract.pop(0)
#for i in spisok_fract:
#    if i > max_num:
#        max_num = i
#    if i < min_num:
#        min_num = i
#print(max_num - min_num)



#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#def spisok(num, result = ""):
#    if num == 0:
#        return result[::-1]
#    result += str(num%2)
#    return spisok(num//2,result)

#n = int(input())
#print(spisok(n))



#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# def postive_fib(n):
# postive_list = [0,1]
# for i in range(n-1):
# postive_list.append(postive_list[-2]+postive_list[-1])
# return postive_list
#
# def negative_fiv(n):
# negative_list = [0,1]
# for i in range(n-1):
# negative_list.append(negative_list[-2]-negative_list[-1])
# return negative_list
#
#
# print(negative_fiv(8)[::-1] + postive_fib(8)[1:])
