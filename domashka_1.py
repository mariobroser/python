#1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#print("введите день недели")
#a=int(input())
#if a==1:
#    print("понедельник")
#if a==2:
#    print("вторник")
#if a==3:
#    print("среда")
#if a==4:
#    print("четверг")
#if a==5:
#    print("пятница")
#if a==6:
#    print("суббота")
#if a==7:
#    print("воскресенье")
#if a<1 or a>7:
#    print("нет такого дня недели")



#2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#for x in [True,False]:
#    for y in [True,False]:
#        for z in [True,False]:
#            print(x,'AND',y,'OR',z,'=',x and y or z)


#3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#print('Введите координаты точки')
#x = int(input('x= '))
#y = int(input('y= '))
#if x>0:
 #  if y>0:
#       print('Точка лежит в 1 четверти')
#   else:
#       print('Точка лежит в 4 четверти')
#else:
 #  if y>0:
#       print('Точка лежит в 2 четверти')
#   else:
#       print('Точка лежит в 3 четверти')


#4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('Введите четверть')
a=int(input())
if a==1:
    print("x>0;y>0")
if a==2:
    print("x<0;y>0")
if a==3:
    print("x<0;y<0")
if a==4:
    print("x>0;y<0")
if a<1 or a>4:
    print("нет такой четверти оси координат")




#5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#import math
#print('Введите координаты точки A')
#x1 = int(input('x1= '))
#y1 = int(input('y1= '))

#print('Введите координаты точки B')
#x2 = int(input('x2= '))
#y2 = int(input('y2= '))

#p1=[x1,y1]
#p2=[x2,y2]

#distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
#print(distance)
