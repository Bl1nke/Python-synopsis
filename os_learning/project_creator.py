import os

def create_project(name: str):
    if os.path.exitsts(name):
        print("папка с таким название уже существует")
        # return досрочно выходит из функции не создавай ничего
        return
        
    project_structure = [
        (os.path.join(name, 'src', '__init__.py'), None),
        (os.path.join(name, 'src', 'main.py'), f'print("Привет от {name}")'),
        (os.path.join(name, 'tests', 'test_main.py'), 'Тесты тут'),
        (os.path.join(name, 'data', '.gitkeep'), None),
        (os.path.join(name, 'requirements.txt'), 'Требования'),
        (os.path.join(name, 'README.md'), '# Имя проекта'),
    ]
    
    
    created_files = []

    for file_path, content in project_structure:
        folder_path = os.path.dirname(file_path)
        os.makedirs(folder_path, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            if content is not None:
                f.write(content)
        # Сохранение пути 
        created_files.append(os.path.abspath(file_path))
    
    print(f"Созданные файлы проекта {name}")
    for path in created_files:
        print(f" - {path}")
    
    # Флаг
    all_exists = True
    # _ значит что это переменная мне не нжуна
    for file_path, _ in project_structure:
        # Проверяет что путь существует и это именно файл
        if not os.path.isfile(file_path):
            print(f"Файл не создан: {file_path}")
            all_exists = False

    if all_exists:
        print("Проект успешно создан")

if __name__ == '__main__':
    project_name = input("Введите имя нового проекта: ").strip()
    if project_name:
        create_project(project_name)
    else:
        print("Имя проекта не может быть пустым.")

# Разобрать каждую строчку и прийти к какому-то пониманию