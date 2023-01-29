def get_op():
    op = int(input(
        '1 - добавить пользователя \n  2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - отсортировать по имени \n 5 - отсортировать по id\n 6 - выход\n'))
    return op

def add_worker():
    id = input()
    name = input()
    lastname = input()
    number = input()
    comments = input()
    line = f"{id},{name},{lastname},{number},{comments}\n"
    with open("worker_list.txt","a") as file:
        file.write(line)
    print("сохранено!!!")

def print_table():
    with open("worker_list.txt","r") as file:
        for line in file.readlines():
            print(line,end="")

def print_only_name():
    with open("worker_list.txt","a") as file:
        lst = ile.readlines()
        for line in lst:
            a = line.split(",")
            print(f"имя - {a[1]}, фамилия - {a[2]}")
