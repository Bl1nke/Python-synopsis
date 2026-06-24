import os


# Показывает путь откуда в терминале запускается скрипт
current_dir = os.getcwd()
print(f"Текущая папка {current_dir}")


os.chdir('..')  # Подняться на папку вверх
os.chdir('/path/to/folder')  # Перейти в конкретную папку


# просмотр содержимого
files_and_dirs = os.listdir('.') # Точка означает текущую папку
print(f"Содержимое: {files_and_dirs}")


# Создание папок

os.mkdir('new_folder')

# Создание вложенных папок
os.makedirs('project/test')

# Удаление папок
os.rmdir('new_folder')       # Удалит только если папка ПУСТАЯ
os.removedirs('project/src/utils') # Удалит всю цепочку пустых папок


# Переименовывание папок

os.rename('old.txt', 'new.txt')

# Подмодуль os.path

# правило: Не склеивать пути вручную через строки("folder" + "/" + "dile.txt") использовать os.path

# Правильное склеивание путей
path = os.path.join('my_folder', 'sub_folder', 'file.txt')
print(path)


# Разбор пути на части

my_path = '/home/user/documents/report.pdf'

print(os.path.dirname(my_path))   # /home/user/documents (только папка)
print(os.path.basename(my_path))  # report.pdf (только имя файла)
print(os.path.splitext(my_path))  # ('/home/user/documents/report', '.pdf')


# Проверка существует ли файл
print(os.path.exists('my_folder'))

# Удаление файлов
os.remove('name.txt')
# Удаляет безвазвратно минуя корзину

all_vars = os.environ

print(all_vars)

print(os.name)
#  Выводит nt, так как windows. NT расшифровывается как New Technology

print(os.sep) 
# Разделитель путей 

os.system('dir')

os.system('ping google.com')
