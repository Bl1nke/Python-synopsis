import uuid


# Версия 4 генерируется на основе случайных чисел, используется 95 % времени
my_num = uuid.uuid4()

print(my_num)
print(type(my_num))

# Чтобы сохранить его в базу данных или передать по сети нужно превратить его в строку

uuid_string = str(my_num)
print(type(uuid_string))

# Версия 1 использует MAC адресс и текущее время
# Плохо для приватности, так как раскрывает MAC
# Можно сортировать по времени создания

uuid_v1 = uuid.uuid1()
print(uuid_v1)


# Версия 3 и 5 (Детерминированные - значит полное и предсказуемое поведение)
# Генерируется путем хэширования(перемалывания) како-то текста, например url
# Если дать один и тот же текст, то получим один и тот же результат

namespace = uuid.NAMESPACE_DNS
# namespace дает уникальный контекст для генерации UUID
# Есть хороший пример для понимания
# Пространство имен для текста=Александра
# Имя: Александра, Город: Александра (Тоесть уникальный контекст)
# для разных namespace uuid будет разный



text = "Example.com"

uuid_v5 = uuid.uuid5(namespace, text)
print(uuid_v5)


my_uuid = uuid.UUID('123e4567-e89b-12d3-a456-426614174000')

print(my_uuid.hex)
print(my_uuid.int)

unid_text = "123e4567-e89b-12d3-a456-426614174000"

temp = uuid.UUID(unid_text)
print(temp)
print(type(temp))
print(temp.version)

