import json

while True:
    print("Показать задачи|Добавить задачу|Выполнить|Выход")
    user_input = input("Что вы хотите сделать? ")
    if user_input == "Показать задачи":
        try:
            with open("json_learning/tasks.json", "r", encoding='utf-8') as file:
                data = json.load(file)
                for index, item in enumerate(data):
                    task_id = item.get("id")
                    task_text = item.get("text")
                    task_status = item.get("status")
                    if index == 0:
                        print("Список задач:")
                    print(f"---Задача номер {task_id}: {task_text}. Статус {task_status}")
        except(FileNotFoundError, json.JSONDecodeError):
            print("Список задач отсутсвует или неисправлен")
    elif user_input == "Добавить задачу":
        task_text = input("Введите название задачи: ")
        num = int(input("Введите номер задачи: "))
        task = {"id": num, "text": task_text, "status": False}
        try:
            with open("json_learning/tasks.json", "r", encoding='utf-8') as file:
                data = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append(task)
        with open("json_learning/tasks.json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            print("Задача добавлена")
    elif user_input == "Выполнить":
        class WrongID(Exception):
            pass
        try:
            task_num = int(input("Введите номер задачи: "))
            with open("json_learning/tasks.json", "r", encoding='utf-8') as file:
                data = json.load(file)
                for index, item in enumerate(data):
                    task_id = item.get("id")
                    if task_num == task_id:
                            with open("json_learning/tasks.json", "w", encoding='utf-8') as file:
                                task_status = True
                                data = json.dump(data, file)
                                print(f"---Задача номер {task_id}: {task_text}. Статус {True}")
        except(FileNotFoundError, json.JSONDecodeError):
            print("Список задач пуст или неисправен")
        except WrongID:
            print("Неверный номер задачи")
    elif user_input == "Выход":
        print("Работа завершена")
        break
    else:
        print("Такой команды пока нет, выберете из существующих")
# Можно ли вместо создания своей ошибки просто вывести принт, что такой ошибки не существует





  







