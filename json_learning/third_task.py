import json

with open("json_learning/users.json", "r", encoding="utf-8") as file:
    # json.load автоматически определяет структуру json файла
    data = json.load(file)
    # enumerate позволяет нам создать index для автоматического подсчета количества(счетчик элементов + автоматическое увелечение счетчика +=1)
    for index, item in enumerate(data):
        user_id = item.get("id")
        user_login = item.get("login")
        user_status = item.get("is_active")

        print(f"Пользователь {user_login} с id {user_id} со статусом {user_status}")
                

Bill_data = {"id": 4324, "login": "Билл", "is_active": True}

data.append(Bill_data)

with open("json_learning/users.json", "w", encoding="utf-8") as file:
    # json.dump принимает два обязательных позиционных аргумента(что сохранять и куда сохранять)    
    json.dump(data, file, indent=2, ensure_ascii=False)
    print("Пользователь добавлен")

