import json

# data_dict = {"name": "Bill", "age": 20, "hobby": ["football, running"], "married": True, "pet": None}

# print(type(data_dict["hobby"]))

# json_data_dict = json.dumps(data_dict)
# print(type(json_data_dict))
# print(json_data_dict)

# reverse_to_dict = json.loads(json_data_dict)
# print(type(reverse_to_dict["hobby"]))


data1_dict = ("Bill", 20, ["football, running"], True)
print(type(data1_dict))
print(data1_dict)

json_data1_dict = json.dumps(data1_dict)
print(type(json_data1_dict))
print(json_data1_dict)

reverse_to_dict1 = json.loads(json_data1_dict)
print(type(reverse_to_dict1))
print(reverse_to_dict1)

# Из кортежа получается лист