import os
import shutil
import platform

def create_folder():
    folder_name = input("Введите название папки: ")
    try:
        os.mkdir(folder_name)
        print(f'Папка "{folder_name}" успешно создана!')
    except FileExistsError:
        print("Ошибка: Папка уже существует!")

def delete_file_or_folder():
    name = input("Введите название файла или папки для удаления: ")
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f'Папка "{name}" удалена!')
    elif os.path.isfile(name):
        os.remove(name)
        print(f'Файл "{name}" удален!')
    else:
        print("Ошибка: Файл или папка не найдены!")

def copy_file_or_folder():
    src = input("Введите название файла или папки для копирования: ")
    dst = input("Введите новое название файла или папки: ")
    if os.path.isdir(src):
        shutil.copytree(src, dst)
        print(f'Папка "{src}" скопирована в "{dst}"!')
    elif os.path.isfile(src):
        shutil.copy2(src, dst)
        print(f'Файл "{src}" скопирован в "{dst}"!')
    else:
        print("Ошибка: Файл или папка не найдены!")

def list_directory():
    print("Содержимое директории:", os.listdir())

def list_folders():
    print("Папки:", [f for f in os.listdir() if os.path.isdir(f)])

def list_files():
    print("Файлы:", [f for f in os.listdir() if os.path.isfile(f)])

def os_info():
    print("Операционная система:", platform.system(), platform.release())

def creator_info():
    print("Программа создана пользователем: Your Name")

def play_quiz():
    print("Игра 'Викторина' пока не реализована")

def bank_account():
    print("Функция 'Банковский счет' пока не реализована")

def change_directory():
    new_path = input("Введите путь к новой рабочей директории: ")
    try:
        os.chdir(new_path)
        print("Рабочая директория изменена на", os.getcwd())
    except FileNotFoundError:
        print("Ошибка: Директория не найдена!")

def main():
    while True:
        print("""
        1. Создать папку
        2. Удалить (файл/папку)
        3. Копировать (файл/папку)
        4. Просмотр содержимого директории
        5. Посмотреть только папки
        6. Посмотреть только файлы
        7. Информация об ОС
        8. Создатель программы
        9. Играть в викторину
        10. Мой банковский счет
        11. Смена рабочей директории
        12. Выход
        """)
        choice = input("Выберите действие: ")
        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file_or_folder()
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            list_directory()
        elif choice == "5":
            list_folders()
        elif choice == "6":
            list_files()
        elif choice == "7":
            os_info()
        elif choice == "8":
            creator_info()
        elif choice == "9":
            play_quiz()
        elif choice == "10":
            bank_account()
        elif choice == "11":
            change_directory()
        elif choice == "12":
            print("Выход из программы")
            break
        else:
            print("Ошибка: Некорректный ввод, попробуйте снова")

if __name__ == "__main__":
    main()
