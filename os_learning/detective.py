import os

# откуда запущен скрипт
current_dir = os.getcwd()

# Где физически лежит скрипт
script_full_path = os.path.abspath(__file__)
# Отрезаем имя файла, оставив только папку
script_dir = os.path.dirname(script_full_path)

print(f"Текущая рабочая папка: {current_dir}")
print(f"Папка скрипта: {script_dir}")


if current_dir == script_dir:
    print("yes")
else:
    print("no")
# Полный путь к файлу 
secret_path = os.path.join(script_dir, "secret.txt")

if os.path.isfile(secret_path):
    print(f"Файл найден {secret_path}")
else:
    print("Файл не найден")