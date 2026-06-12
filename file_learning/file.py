
# КОНЕЧНО ЖЕ НУЖНО УКАЗЫВАТЬ ПОЛНЫЕ ПУТИ К ФАЙЛАМ ДЛЯ РАБОТЫ ПРОГРАММЫ


# # Чтение файла, выводит построчно
with open("text.txt", 'r') as text:
    line = text.read()
    print(line)


# print("_________________________")

# Чтение файла, выводит список из существующих строк
with open("text.txt", "r") as text_1:
    lists = text_1.readlines()
    print(lists)


# print("_________________________")

# Здесь мы записываемШ(при этом автоматически создается новый файл), а затем читаем
with open("test.txt", "w") as f:
    f.write("New string\n")
    f.write("Did you i think i forgotten you?\n")

# # Добавили новую строку в сущетсвующий файл
with open("test.txt", "a") as f:
    f.write("append new string\n")

# # writelines удaляет все то, что уже было
list = ["FU2024\n", "Biozare\n"]
with open("test.txt", "a") as f:
    f.writelines(list)

with open("test.txt", "r") as f:
    lines = f.read()
    print(lines)

# print("_______________________")

list = ["FU2024\n", "Biozare\n"]
with open("test.txt", "w") as f:
    f.writelines(list)


with open("test.txt", "r") as f:
    lines = f.read()
    print(lines)


# Приклaдные задания от DeepSeek

# 1
with open("hello.txt" , "w") as file:
    file.write("Привет, Мир")

with open("hello.txt", "r") as file:
    line = file.read()
    print(line)

# 2


# Здесь мы добавляем в файл строку каждый раз + сохранение существующего текста
while True:
    user_input = input()
    if user_input != "":
        with open("u_text.txt", "a") as u_text:
            u_text.write(user_input + "\n")
    else:
        break

with open("u_text.txt", "r") as u_text:
    o_line = u_text.read()
    print(o_line)

# здесь файл перезаписывается каждый раз и там только новые данные
with open('u_text.txt', 'w') as f:
    while True:
        line = input("Введите строку (Enter для выхода): ")
        if line == "":
            break
        f.write(line + '\n')


# 3

with open("num.txt", "r") as file:
    nums = file.readlines()

clean_num = [x.replace("\n", "") for x in nums]

int_num = []

for num in clean_num:
    new_num = int(num)
    int_num.append(new_num)

total = sum(int_num)

with open("sum.txt", "w") as file:
    file.write(str(total))

# 4

from datetime import datetime

while True:

    user_input = input()

    if user_input == "выход":
        break


    elif user_input == "история":
        try:
            with open("log.txt", "r", encoding="utf-8") as file:
                logs = file.read()
                if logs:
                    print(logs)
                else:
                    print("Лог пуст")
        except FileNotFoundError:
            print("файла лога не существует")
    
    else:
        now = datetime.now()
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f"{user_input} [{now}]\n")
        print("Данные сохранены")