# Вызов функции
def greet(name):
    print(f"Hello my dear {name}")

greet("John")

# Автоматическая упаковка в кортеж
def get_user_info():
    return "ivan", 25, "Moscow"

name, age, city = get_user_info() # Возовращает кортеж данных

print(name)
print(get_user_info())

# Параметры и аргументы
# Параметры — это переменные в скобках при объявлении функции.
# Аргументы — это фактические значения, передаваемые при вызове.
# В данном случае мы имеем значение по умолчанию для exp

# Виды аргументов:

#     Позиционные: передаются в том же порядке, в котором объявлены параметры.
#     Именованные (keyword): передаются с указанием имени параметра (greet(name="Иван")).
#     Со значением по умолчанию: если аргумент не передан, используется значение по умолчанию. Важно: 
# параметры со значением по умолчанию должны идти после обязательных параметров


def power(base, exp=2):
    return base ** exp

print(power(2))
print(power(3, 3))

# Произвольное количество агрументов *args и **kwargs
# *args собирает все переданные позиционные аргументы в кортеж
# **kwargs собирает все переданные именованные аргументы в словарь

def print_info(*args, **kwargs):
    print("Позиционные: ", args)
    print("Именнованые: ", kwargs)

print_info(1, 2, 3, name = "Ann", age = 30, city = "NY")
print_info(7,8,9, "glev", "sup")


# Область видимости

# Python использует правило LEGB для поиска переменных:

#     Local (локальная) — внутри текущей функции.
#     Enclosing (вложенная) — в функциях, охватывающих текущую (для вложенных функций).
#     Global (глобальная) — на уровне модуля.
#     Built-in (встроенная) — встроенные имена Python (например, len, print).

# Ключевые слова для изменения области видимости:

#     global: позволяет изменять глобальную переменную внутри функции.
#     nonlocal: позволяет изменять переменную из внешней (но не глобальной) функции.

x = "global"

def outer():
    x = "Enclosing"
    def inner():
        # nonlocal вынуждает x быть равным "local" в outer
        # он говорит x что не нужно создавать новую переменную, а следует привязаться к ближайшей x
        # из внешней функции, тоесть outer. Теперь оба x ссылаются на один и тот же объект памяти
        # доказно с помощью функции id()
        nonlocal x
        x = "local"
        print("in inner ", x)
        print(id(x))
    inner()
    print("in outer ", x)
    print(id(x))

outer()


# global 

# без global

count = 0

def increment():
#     # Создается новая локальная переменная count
    count = 1
    print(count)

increment()
print(count) # Выводиться глобальная переменная

# С global

count = 0

def increment():
    global count
    count +=1
    print(count)

increment()
print(count) # Изменилась глобальная переменная

# Анонимные функции lambda
# Использовать только тогда когда можно поместить в одну простую конструкцию

square = lambda x: x ** 2
print(square(5))

pairs = [(1, "one"), (3, "three"), (2, "two")]
pairs.sort(key=lambda pair: pair[0])
print(pairs)


# Функции как объекты в других функциях

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def process_to_text(func, text):
    return func(text)

#  Передаем функцию как один из аргументов
print(process_to_text(whisper, text="FDSFDSF"))


# Декарторы
# Декоратор — это функция, которая принимает другую функцию и расширяет её поведение,
#  не изменяя её код напрямую. Используется синтаксис @.

def my_decarator(func):
    def wrapper():
        print("Действие до вызова функции")
        func()
        print("Действие после вызова функции")
    return wrapper


@my_decarator
def say_hello():
    print("Привет")


say_hello()

# Type hints и Docstring указание типов для читаемости и проверки
def calculate_area(radius: float) -> float:
    import math
    result = math.pi * (radius ** 2)
    print(result)

calculate_area(4)
