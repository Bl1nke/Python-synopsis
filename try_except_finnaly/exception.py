# while True:
#     try:
#         user_num = int(input("Введите целое число "))
#         print(f"Число пользователя {user_num}")
#     except ValueError:
#         print(f"не является целым числом, попроубуйте снова")

# Если сделать сразу user_num = int(input("Введите число ")), то при ошибке переменная не будет созадана
# значит в блоке except не будет переменной, поэтому деалем по шагам как снизу. только ЕСЛИ НАМ НАДО ВЫВЕСТИ ДАННЫЕ
# В БЛОКЕ EXCEPT

# while True:
#     try:
#         user_input = input("Введите число ")
#         user_num = int(user_input)
#         print(f"Число пользователя {user_num}")
#     except ValueError:
#         print(f"{user_input} не является целым числом, попроубуйте снова")

# несколько исключений: 

try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    result = a / b
    print(result)
except ValueError:
    print("Было введно не число")
except ZeroDivisionError:
    print("Деление на ноль запрещено")

# Перехвад нескольких исключений в одном блоке

try:
    risky_code()
except (ValueError, KeyError, TypeError):
    print("Одно из трех исключений")

# Доступ к объективу исключения (Сохранить объект этой ошибки в переменную e)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Поймана ошибка {e}")
    # Тип ошибки
    print(f"Тип ошибки: {type(e).__name__}")



# в try код, который может упасть, а в else уже то, что будет после успешного испольнения try
try:
   file = open("C:/learning_python/try_except_finnaly/data.txt", 'r')
except FileNotFoundError:
   print("Файл не был найден")
else:
   content = file.read()
   print(content)
# finnaly исполняется всегда в независимости от было исключение или нет
finally:
   file.close()

# raise нужен для того, чтобы создать свою ошибку. Здесь мы создаем собвственное исключение

class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"Возраст не может быть отрицательным ({age})")
    print("Возраст установлен")

try:
    set_age(-5)
except NegativeAgeError as e:
    print(f"Возникла ошибка \n {e}")


# Практические задания от deepseek
# Калькулятор с обработкой ошибок

print("Кальулятор: (+, -, *, /) ")

try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
except ValueError:
    print("введено не целое число")
    exit()

class WrongZnak(Exception):
    pass
try:
    znak = input("Введите операцию ")
    if znak not in ['+', '-', '*', '/']:
        raise WrongZnak
except WrongZnak:
    print("Неверная операция")
else:
    try:
        result = eval(f"{a} {znak} {b}")
    except ZeroDivisionError:
        print("Деление на ноль запрещено")
    else:
        print(result)


#Чтение конфигурационного файла

config = {"host": "localhost", "post" : 5000}

def get_key(key):
    if key not in config:
        raise KeyError(f"Ключ {key} отстутсвует в конфигурации")
    return config[key]


try:
    print(get_key("host"))
    print(get_key("username"))
except KeyError as e:
    print(f"Конфигурационная ошибка: {e}")
finally:
    print("Конфигурация проверена")
    
