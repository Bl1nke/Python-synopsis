# match переменная:
#     case значение_1:
#         # код, если переменная == значение_1
#     case значение_2:
#         # код, если переменная == значение_2
#     case _:
#         # код по умолчанию (аналог default в других языках)


# status_code = 200

# match status_code:
#     case 200:
#         print("Good")
#     case 404:
#         print("Error")
#     case 500:
#         print("error 2")
#     case _:
#         print("Default") 

# day = "суббота"

# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница":
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Это выходной!")
#     case _:
#         print("Неправильный день")

command = ["save", "file.txt", "backup.txt"]

match command:
    case ["exit"]:
        print("Выход из программы")
    case ["save", filename]:
        print(f"Сохраняем файл как {filename}")
    case ["save", source, destination]:
        print(f"Копируем {source} в {destination}")
    case _:
        print("Неизвестная команда")