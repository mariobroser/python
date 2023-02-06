def get_op():
    op = int(input("1 - д.с, 2 - д.п, 3 - д.о, 4 -показ список, 5 -показать конк сп,  6 -выход"))
    return op

def input_student():
    name = input("Введите имя и фамилию")
    return name

def input_less():
    less = input ("Введите предмет")
    return less

def input_mark():
    name = input("введите имя")
    less = input("введите предмет")
    mark = input("введите оценку")
    return name,less,mark

def get_name_to_show():
    name = input("введите имя для просмотра оценок")
    return name
