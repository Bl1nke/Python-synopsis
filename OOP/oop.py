# Класс описывает какимим данными и действиями будет обладать объект
# Объект это конкретная сущность в памяти пк созданная на основе класса


class Dog:
    # Это специальный метод-конструктор. Он запускается АВТОМАТИЧЕСКИ 
    # при создании нового объекта (собаки).
    def __init__(self, name, breed):
        # self — это ссылка на КОНКРЕТНЫЙ создаваемый объект.
        # Мы сохраняем переданные данные внутрь этого объекта.
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) говорит ГАВ")



dog1 = Dog(name="Silly", breed="litle puppy")
dog1.bark()

# self можно представить как слово мой. когда dog1.bark() вызывает метод, то Python неявно передает dog1
# как первый агрумент. Внутри метода self.name означает "Имя этой конкретной собаки"

# Атрибуты и Методы

# Атрибуты — это переменные, которые хранят состояние объекта (имя, возраст, цвет, баланс счета).
# Методы — это функции, которые описывают поведение объекта (лаять, бежать, положить деньги на счет).
# Они всегда принимают self первым параметром.

# Вся мощь ООП держится на четырех принципах.

# 1 Инкапсуляция(Соекрытие данных)

# Мы прячем внутреннее устройство объекта и защищаем данные от прямого изменения извне
# доступ должен идти через специальные методы

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # Два подчеркивания __ делают атрибут "приватным" (скрытым)
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено на {amount}. Новый баланс {self.__balance}")
        else:
            print("Сумма должна быть положительной")

    def get_balance(self):
        return self.__balance
    

# account.__balance = 999999  # ОШИБКА! Мы не можем изменить баланс напрямую

account = BankAccount(owner="Ivan", balance=1000)
print(account.get_balance())
account.deposit(1200)
print(account.get_balance())

# Нужно чтобы никто случайно не обнулил баланс и не записал туда отрицательное число


# 2 Наследование

# возможность создавать новый класс на основе сущесвтующего, чтобы не писать один и тот же код дважды.
# Новый класс получает все атрибудт и методы старого


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} кушает")

# Дочерний класс наследует от Animal
class Cat(Animal):
    def __init__(self, name, color):
        # super() вызывает метод __init__ родительского класса
        super().__init__(name)
        self.color = color
    
    def meow(self):
        print(f"{self.name} ({self.color}) говорит Мяу")


cat = Cat(name="barsik", color="black")
cat.eat() # Этот метод унаследован от Animal
cat.meow()

# 3 Полиоморфизм

# Суть: "множество форм" Возможность использовать объекты разных классов через один и тот же интерфейс
# (Одинаковые названия методов)

class Dog:
    def speak(self):
        return "Bark"
    
class Cat:
    def speak(self):
        return "Meow"
    
class Duck:
    def speak(self):
        return "Kria"
    
# Функция, которая не знает, кто к ней придет, но знает, что у всех есть метод speak()
def make_it_speak(animal):
    print(animal.speak())


animals = [Dog(), Cat(), Duck()]

for animal in animals:
    make_it_speak(animal)



# 4 Абстракция

# выделение главных характеристик объекта и игнорирование неважных деталей. В коде это реализуется
# через абстрактные классы(Шаблоны), которые нельзя создать напрямую, но от которых нужно наследоваться


from abc import ABC, abstractmethod

# ABC = Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # Мы только объявляем, что метод должен быть, но не пишем, как он работает

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Мы ОБЯЗАНЫ реализовать этот метод, иначе Python выдаст ошибку
    def area(self):
        return 3.14 * (self.radius ** 2)
    
# shape = Shape() # ОШИБКА! Нельзя создать объект абстрактного класса
circle = Circle(5)
print(circle.area())

# Зачем это нужно? Чтобы задать строгий контракт для разработчиков:
# "Если ты создаешь фигуру, у нее обязательно должен быть метод area()".

# Практические задания

class Smartphone:
    def __init__(self, brand, battery_level):
        self.brand = brand
        self.__battery_level = battery_level

    def charge(self):
        print(f"Заряд батареи {self.__battery_level} %")
        while self.__battery_level < 100:
            self.__battery_level += 5
            if self.__battery_level > 100:
                self.__battery_level = 100
            print(f"Заряжается телефон {self.brand} равен {self.__battery_level} %")

    def make_call(self, name):
        if self.__battery_level < 5:
            print(f"{self.brand} разряжен!")
        self.__battery_level -= 5
        print(f"Звонил по телефону {self.brand} осталось: {self.__battery_level} %. контакту {name}")



Iphone17 = Smartphone(brand="Iphone 17", battery_level= 83)

Iphone17.charge()

Iphone17.make_call(name="Egor")


class Wallet:
    def __init__(self, gold):
        self.__gold = gold

    def earn(self, amount):
        if amount > 0:
            self.__gold += amount
            print(f"Добавили золотишка в размере {amount}")
        else:
            print("Добыча не может быть отрицательной")

    def spend(self, amount):
        if amount > self.__gold:
            print("Столько забрать не выйдет")
        else:
            self.__gold -= amount
            print(f"Потратили {amount} золотишка")

    def get_balance(self):
        print(f"Текущее количество золота {self.__gold}")

    def __str__(self):
        return f"💰 Кошелёк: {self.__gold} золота"


w = Wallet(100)
w.get_balance()
w.earn(50)       # +50
w.spend(30)      # -30
print(w)         # 💰 Кошелёк: 120 золота
w.spend(200)
w.__gold = 99999