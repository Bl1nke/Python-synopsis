import json
book_dict = {"Название": "Война и Мир", "Автор" : "Лев толстой", "Год выпуска" : 1787, "Жанры": ["Драма", "Роман"]}
# sort_keys сортирует ключи по алфавиту
book_dict_json = json.dumps(book_dict, indent=4, ensure_ascii=False, sort_keys=True)

print(book_dict_json)

