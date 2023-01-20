#38.Напишите программу, удаляющую из текста все слова, содержащие ""абв""
#word = input("Введите слова через пробел:\n")
#print(f"Слово: {word}")
#find_word = "абв"
#lst = [i for i in word.split() if find_word not in i]
#print(f'Результат: {" ".join(lst)}')


#39
#from random import randint


#def input_dat(name):
#    x = int(
#        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#    while x < 1 or x > 28:
#        x = int(input(f"{name}, введите корректное количество конфет: "))
#    return x


#def p_print(name, k, counter, value):
#    print(
#        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


#player1 = input("Введите имя первого игрока: ")
#player2 = input("Введите имя второго игрока: ")
#value = int(input("Введите количество конфет на столе: "))
#flag = randint(0, 2)  # флаг очередности
#if flag:
#    print(f"Первый ходит {player1}")
#else:
#    print(f"Первый ходит {player2}")

#counter1 = 0
#counter2 = 0

#while value > 28:
#    if flag:
#        k = input_dat(player1)
#        counter1 += k
#        value -= k
#        flag = False
#        p_print(player1, k, counter1, value)
#    else:
##        counter2 += k
#        value -= k
#        flag = True
#        p_print(player2, k, counter2, value)

#if flag:
#    print(f"Выиграл {player1}")
#else:
#    print(f"Выиграл {player2}")



#41
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
