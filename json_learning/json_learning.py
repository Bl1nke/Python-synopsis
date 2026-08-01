import json

# python_dict = {"name": "Иван", "age": 30, "is_working": True}

# Здесь мы переводим строку python(словарь ключ значение в строку json) 
# Это называется Сериализация
# ensure_ascii=False позволяет нам получать кирилицу в строки формата json
# json_string = json.dumps(python_dict, ensure_ascii=False)
# print(type(json_string))
# print(json_string)

# Здесь мы переводим строку json в словарь ключ значение
# Это называется Десириализация
# new_dict = json.loads(json_string)
# print(type(new_dict))
# print(new_dict)

# data = {"city": "Москва", "population": 12000000}

# with open("data.json", "w", encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False)

# with open("json_learning/data.json", "r", encoding='utf-8') as file:
#     data = json.load(file)
#     print(data["city"])

# Обработка ошибок json если он битый
bad_json = '{"name": "Иван", "age": 30'
try:
    data_1 = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"Ошибка при чтении JSON {e}")

    