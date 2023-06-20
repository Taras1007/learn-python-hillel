import os

def home_screen():
    """
    Функція має 4 блока які при визову переходять на відповідний інструментарій
    При вибиранні команди з function_home_screen переходить на выдповідну функцію
    while застосовуєься для перевірки коректного вводу
    """
    print("Головне меню")
    function_home_screen = input("Вибери зі списку що хочеш зробити:\n"
                                 "add - додати файл для нотаток.\n"
                                 "add note - додати нотатку.\n"
                                 "del file - видалити файл.\n"
                                 "del note - видалити нотатку\n"
                                 "view - щоб переглянути нотатки.\n"
                                 "quit - щоб вийти з програми.\n"
                                 "Напиши варіант сюди: ")
    # Перехід на відповідну вкладку з застосуванням некоректного вводу
    while True:
        if function_home_screen.lower() == "add":
            append_file()
        elif function_home_screen.lower() == "add note":
            append_note_with_file()
        elif function_home_screen.lower() == "del file":
            del_file()
        elif function_home_screen.lower() == "del note":
            del_note_with_file()
        elif function_home_screen.lower() == "view":
            view_note()
        elif function_home_screen.lower() == "quit":
            quit_program()
        else:
            print("Не зрозумів вас.")
        function_home_screen = input("Повторіть ще раз.\n")

def append_file():
    """
    Функція додавання нового файлу для зберігання в ньому нових нотаток
    :return: Повертає на головне меню
    """
    name_file = str(input("Введи назву нового файлу для збереження нотаток: "))
    # Додавання файлу
    with open(f"{name_file}.txt", "a") as f:
        home_screen()

def append_note_with_file():
    """
    Функція перевіряє наявність всіх файлів .txt, якщо такі є виводить на екран, якщо ні повертає на головну сторінку
    При виведені на екран користувач вибирає файл в який добавляє нотатку
    :return: Повертає на головне меню
    """
    directory = "/Users/taraspetruk/PycharmProjects/pythonProject1"
    files = os.listdir(directory)
    # Перевірка на наявність файлів
    if not any(file.endswith(".txt") for file in files):
        print("У вас немає файлів, добавте файл.")
        home_screen()
    print("Всі ваші файли з нотатками:")
    # Виведення файлів на екран
    for file in files:
        if file.endswith(".txt"):
            print(file)
    input_name_file = str(input("Вибери файл в який додади нотатку: "))
    # Додавання нотатків
    with open(input_name_file, "a") as f:
        new_note = str(input("Введи нову нотатку: "))
        f.write(new_note + "\n")
    home_screen()

def del_file():
    """
    Функція видалення файлу, перевірка на наявність, вивід на екран
    Користувач вводить який файл потрібно видалити
    :return: Повертає на головний екран
    """
    directory = "/Users/taraspetruk/PycharmProjects/pythonProject1"
    files = os.listdir(directory)
    # Перевірка на наявність файлу
    if not any(file.endswith(".txt") for file in files):
        print("У вас немає файлів, добавте файл.")
        home_screen()
    # Виведення файлів на екран
    for file in files:
        if file.endswith(".txt"):
            print(file)
    # Видалення файлу
    while True:
        try:
            name_file_del = str(input("Введіть назву файлу для видалення: "))
            os.remove(name_file_del)
            break
        except FileNotFoundError:
            print("Не вдвлося знайти файл")
        except Exception:
            print("Не вдвлося знайти файл.")
            name_file_del = str(input("Введіть назву файла для видалення: "))
    home_screen()

def del_note_with_file():
    """
    Функція видалення нотатки з файлу. Перевірка на наявність файлів.
    Користувач вводить назву файлу і вибирає яку нотатку потрібно видалити
    :return: Повертає на головний екран
    """
    directory = "/Users/taraspetruk/PycharmProjects/pythonProject1"
    files = os.listdir(directory)
    # Перевірка на наявність файлу
    if not any(file.endswith(".txt") for file in files):
        print("У вас немає файлів, добавте файл.")
        home_screen()
    # Виведення файлів на екран
    for file in files:
        if file.endswith(".txt"):
            print(file)
    # Пошук файлу
    while True:
        try:
            name_file_open = str(input("Введіть назву файлу для відкриття: "))
            with open(name_file_open, "r") as f:
                list_note = f.readlines()
                for index, i in enumerate(list_note):
                    print(index, i.strip())
                break
        except FileNotFoundError:
            print("Не вдалося знайти файл")
        except Exception:
            print("Не вдалося знайти файл")
    # Пошук нотатки по індексу для видалення
    index_note_del = int(input("Введи індекс нотатки яку потрібно видалити: "))
    del list_note[index_note_del]
    # Зберігання після редагування
    with open(name_file_open, "w") as f:
        f.writelines(list_note)
    print("Нотатку видалено")
    home_screen()

def view_note():
    """
    Функція перевіряє на наявність файлів з нотатками.
    Якщо такі є виводить на екран варіанти показу нотаток
    Виводить нотатки в такоому порядку який вибрав користувач
    :return: Повертає на головний екран
    """
    directory = "/Users/taraspetruk/PycharmProjects/pythonProject1"
    files = os.listdir(directory)
    # Перевірка на наявність файлу
    if not any(file.endswith(".txt") for file in files):
        print("У вас немає файлів, добавте файл.")
        home_screen()
    directory = "/Users/taraspetruk/PycharmProjects/pythonProject1"
    files = os.listdir(directory)
    print("Всі ваші файли з нотатками:")
    # Виведення на екран всіх файлів
    for file in files:
        if file.endswith(".txt"):
            print(file)
    # Відкриття відповідної нотатки
    input_file = str(input("Виберіть нотатку для відкриття: "))
    with open(input_file, "r") as f:
        text = f.readlines()
    # Виведення нотаток на екран
    command = input("Введіть команду в якому вигляді вивести нотатки (earliest, latest, longest, shortest): ")
    if command.lower() == "earliest":
        print("Збережені нотатки у хронологічному порядку (від найранішої до найпізнішої):")
        for index, note in enumerate(text):
            print(index, note.strip())
    elif command.lower() == "latest":
        print("Збережені нотатки у хронологічному порядку (від найпізнішої до найранішої)")
        for note in reversed(text):
            print(note.strip())
    elif command.lower() == "longest":
        print("Збережені нотатки у порядку їх довжини (від найдовшої до найкоротшої):")
        for note in sorted(text, key=len, reverse=True):
            print(note.strip())
    elif command.lower() == "shortest":
        print("Збережені нотатки у порядку їх довжини (від найкоротшої до найдовшої):")
        for note in sorted(text, key=len, reverse=False):
            print(note.strip())
    home_screen()

def quit_program():
    """
    Функція виходу з програми.
    :return: quit with program
    """
    quit()

# Запуск програми
if __name__ == '__main__':
    home_screen()