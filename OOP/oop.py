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


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} едет со скоростью {self.speed}")


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors


class Airplane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude

    def move(self):
        print(f"{self.brand} летит со скоростью {self.speed} на высоте {self.altitude} м")

class Bicycle(Vehicle):
    # def __init__(self, brand, speed):
    #     super().__init__(brand, speed)
    
    # def move(self):
    #     print(f"{self.brand} едет со скоростью {self.speed}")
    pass
    # Конструктор и move() автоматически наследуются поэтому их можно не писать, тем более что функционал одинаковый

car = Car("BMW", 120, 4)
plane = Airplane("Boeing", 900, 10000)
bike = Bicycle("Giant", 25)

car.move()    # BMW едет со скоростью 120 км/ч
plane.move()  # Boeing летит на высоте 10000 м
bike.move()   # Giant едет со скоростью 25 км/ч



class CreditCard:
    def pay(self, amount):
        return f"💳 Оплата картой на {amount}₽. Последний номер: 4242"

class PayPal:
    def pay(self, amount):
        return f"📧 Оплата через PayPal на {amount}₽. Email: user@mail.com"

class Crypto:
    def pay(self, amount):
        return f"₿ Оплата в Bitcoin на {amount}₽."


def checkout(payment_method, amount):
    print(payment_method.pay(amount))


payment_methods = [CreditCard(), PayPal(), Crypto()]

for payment_method in payment_methods:
    checkout(payment_method, 500)


checkout(CreditCard(), 1500)   # 💳 ...
checkout(PayPal(), 2000)       # 📧 ...
checkout(Crypto(), 5000)       # ₿ ...



class CPU:
    def __init__(self, cores, ghz, price):
        self.cores = cores
        self.ghz = ghz
        self.price = price

    def info(self):
        print(f"Процессор обладает {self.cores} ядрами, имеет {self.ghz} частоту и стоит {self.price} $")

class RAM:
    def __init__(self, gb, price):
        self.gb = gb
        self.price = price

    
    def info(self):
        print(f"Оперативная память в размере {self.gb} гб стоит {self.price} $")


class SSD:
    def __init__(self, tb, price):
        self.tb = tb
        self.price = price

    def info(self):
        print(f"Память пк в размере {self.tb} тб и стоит {self.price}")




class Computer:
    def __init__(self, cpu: CPU, ram: RAM, ssd:SSD):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
    
    def show_spec(self):
        print(f"Ваш ПК имеет процессор: {self.cpu.cores} ядер, {self.cpu.ghz} ГГц")
        print(f"Ваша оперативная память: {self.ram.gb} Гб")
        print(f"Ваш SSD: {self.ssd.tb} Тб")

    # property позволяет нам использовать pc.total_price как переменную
    @property
    def total_price(self) -> float:
        return self.cpu.price + self.ram.price + self.ssd.price


cpu = CPU(cores=8, ghz=3.6, price=20000)
ram = RAM(gb=16, price=8000)
ssd = SSD(tb=1, price=10000)

cpu.info()
ram.info()
ssd.info()


pc = Computer(cpu, ram, ssd)
pc.show_spec()
print(f"Общая стоимость ПК: {pc.total_price} $")


class Inventory:
    def __init__(self, all_items:list):
        self.all_items = all_items


    def add_items(self, item:str):
        self.all_items.append(item)
        print(f"Добавлен новый предмет в инветарь! {item}")
    
    def show_items(self):
        print(f"Полный инвентарь: {', '.join(self.all_items)}")

# from abc import ABC, abstractmethod уже есть этот импорт
# нужно было использовать _ а не __, так как обращались к несуществующему объекту _Hero__hp. 
# __ привязывает атрибут к конкретному классу, когда мы пишем self.__hp в Warrior, то python думает, что это 
# только для Warrior и что другие трогать нельзя. При этом когда take_damage(родительский метод) пытается обратиться
# к self.__hp, то он ишет в Hero, там его нет, соответсвенно он его не находит.
# 
# _ не привязывает атрибут ни к какому классу. (Это просто установка для того, чтобы не вмешиваться)



class Hero(ABC):
    def __init__(self, name, inventory_list: Inventory):
        self.name = name
        self.inventory_list = inventory_list

    @abstractmethod
    def attack(self):
        pass


    def take_damage(self, amount):
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0
        print(f"{self.name} получил {amount} урона. Осталось HP: {self._hp}")

    # Нужно для того чтобы можно было узнать текущее здоровье снаружи
    @property
    def hp(self):   
        return self._hp



class Warrior(Hero):
    def __init__(self, name, hp, level, inventory_list: list):
        super().__init__(name, inventory_list)
        self._hp = hp
        self._level = level
        self.inventory_list = Inventory(inventory_list)
    
    def attack(self):
        damage = self._hp * self._level * 0.15
        print(f"{self.name} бьет мечом! с уроном {damage}")
        return damage



class Mage(Hero):
    def __init__(self, name, hp, level, inventory_list : list):
        super().__init__(name, inventory_list)
        self._hp = hp
        self._level = level
        self.inventory_list = Inventory(inventory_list)
    
    def attack(self):
        damage = self._hp * self._level * 0.13
        print(f"{self.name} заклинает! с уроном {damage}")
        return damage


class Archer(Hero):
    def __init__(self, name, hp, level, inventory_list: list):
        super().__init__(name, inventory_list)
        self._hp = hp
        self._level = level
        self.inventory_list = Inventory(inventory_list)
    
    def attack(self):
        damage = self._hp * self._level * 0.25
        print(f"{self.name} бьет мечом! с уроном {damage}")
        return damage



import time

def battle(hero1: Hero, hero2: Hero):
    print(f"Битва между {hero1.name} и {hero2.name}")

    attackers = [hero1, hero2]

    while hero1.hp > 0 and hero2.hp > 0:
        for attacker in attackers:
            defender = hero2 if attacker == hero1 else hero1
            if defender.hp <=0:
                break


        damage = attacker.attack()

        defender.take_damage(damage)

        # Пауза для эффекта
        time.sleep(1) 

    if hero1.hp > 0:
        print(f" {hero1.name} победил! Осталось {hero1.hp}")
    else:
        print(f"{hero2.name} победил! Осталось {hero2.hp}")


inv1 = Inventory(["apple", "sword"])
inv2 = Inventory(["potion"])

warrior = Warrior("Conan", 100, 3, inv1)
mage = Mage("Gandalf", 70, 5, inv2)

battle(warrior, mage)







