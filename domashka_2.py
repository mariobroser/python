#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#num = int(input("Введите целое: "))
#sum = 0
#while (num != 0):
#    sum = sum + num % 10
#    num = num // 10
#print("Сумма цифр числа равна: ", sum)

#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#def mult(n):
#    if n == 1:
#        return 1
#    else:
#        return n * mult(n - 1)

#num = int(input("Введите целое: "))
#list = []
#for e in range(1, num + 1):
#    list.append(mult(e))

#print(f"Произведения чисел от 1 до {num}:  {list}")


#3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#n = int(input())
#list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
#print(f'Последовательность: {list}\nСумма: {round(sum(list), 3)}')



#4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

#n = int(input())
#list_num = [i for i in range(-n,n+1)]
#print(list_num)

#file = open("file.txt", "r")
#a = file.readlines()
#print(a)
#for i in range(len(a)):
#    a[i] = int(a[i].strip())
#print(a)
#
#multi =1
#for i in range(len(a)):
#    multi*=list_num[a[i]]
#print(multi)



#5.Реализуйте алгоритм перемешивания списка.
import random
a =[3,5,6,7,8,9,4,2,3]
random.shuffle(a)
print(a)
