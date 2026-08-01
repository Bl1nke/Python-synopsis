import json

json_text_1 = '{"status": "ok"}'
json_text_2 = '{"status": "ok"'

def parse_json(text:str):
    try:
        data_dict = json.loads(text)
        return data_dict
    except json.JSONDecodeError:
        print("Ошибка парсинга JSON")
        return None
    

print(parse_json(json_text_1))
print(parse_json(json_text_2))