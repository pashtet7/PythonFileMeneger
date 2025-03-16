import os
import shutil
import platform

BALANCE_FILE = "balance.txt"
HISTORY_FILE = "history.txt"

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return float(f.read())
    return 0.0

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return f.read().splitlines()
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        f.write("\n".join(history))

def bank_account():
    balance = load_balance()
    history = load_history()
    while True:
        print(f"\nТекущий баланс: {balance} руб.")
        print("1. Пополнить счет")
        print("2. Совершить покупку")
        print("3. История покупок")
        print("4. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            amount = float(input("Введите сумму пополнения: "))
            balance += amount
        elif choice == "2":
            item = input("Введите название покупки: ")
            price = float(input("Введите сумму покупки: "))
            if price <= balance:
                balance -= price
                history.append(f"{item} - {price} руб.")
                print("Покупка совершена!")
            else:
                print("Недостаточно средств!")
        elif choice == "3":
            print("История покупок:")
            for record in history:
                print(record)
        elif choice == "4":
            save_balance(balance)
            save_history(history)
            print("Баланс и история сохранены.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

def save_directory_list():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    folders = [d for d in os.listdir() if os.path.isdir(d)]
    with open("listdir.txt", "w") as f:
        f.write("Файлы:\n")
        f.write("\n".join(files) + "\n\n")
        f.write("Папки:\n")
        f.write("\n".join(folders) + "\n")
    print("Содержимое директории сохранено в listdir.txt")

def main():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об ОС")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Сохранить содержимое рабочей директории в файл")
        print("13. Выход")

        choice = input("Выберите пункт меню: ")
        if choice == "10":
            bank_account()
        elif choice == "12":
            save_directory_list()
        elif choice == "13":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
