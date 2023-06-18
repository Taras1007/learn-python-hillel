import os

notes = []

def append_note():
    """Функція приймає нову нотатку від користувача і записує її в текстовий файл"""
    with open("my_notes.txt", "a+") as f:
        new_note = str(input("Нова нотатка: "))
        f.write(new_note + "\n")

    # Оновлення списку нотаток
    with open("my_notes.txt", "r") as f:
        notes = f.readlines()

    # Запис файлу після редагування
    with open("my_notes.txt", "w") as f:
        f.writelines(notes)

    view_note()

def del_note():
    """Функція приймає індекс від користувача,
    зчитує всі нотатки і видаляє обрану"""

    with open("my_notes.txt", "r") as f:
        notes = f.readlines()

    # За допомогою циклу проходження по всіх нотатках і вивід на екран
    for index, note in enumerate(notes):
        print(index, note.strip())

    # Перевірка на наявність нотаток
    if not notes:
        print("Немає нотаток")
        view_note()

    # Запит індексу для видалення
    try:
        index_del = int(input("Введіть індекс нотатки яку бажаєте видалити:"))
        del notes[index_del]
        with open("my_notes.txt", "w") as f:
            f.writelines(notes)
    except Exception:
        print("Не вдалося знайти індекс.")
        index_del = int(input("Введіть індекс нотатки яку бажаєте видалити:"))

    print("Нотатку видалено")
    view_note()

def view_note():
    """Функція приймає обраний користувачен
    варіант показу нотаток і виводить н аекран"""
    with open("my_notes.txt", "r") as f:
        notes = f.readlines()

    # Перевірка на правильність вводу
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest, del, exit): ")
        # Зчитує введене значення від користувача і виводить на екран
        if command.lower() == "add":
            append_note()
        elif command.lower() == "earliest":
            print("Збережені нотатки у хронологічному порядку (від найранішої до найпізнішої):")
            for index, note in enumerate(notes):
                print(index, note.strip())
        elif command.lower() == "latest":
            print("Збережені нотатки у хронологічному порядку (від найпізнішої до найранішої):")
            for index, note in enumerate(reversed(notes)):
                print(f"{index}. {note.strip()}")
        elif command.lower() == "longest":
            print("Збережені нотатки у порядку їх довжини (від найдовшої до найкоротшої):")
            for note in sorted(notes, key=len, reverse=True):
                print(note.strip())
        elif command.lower() == "shortest":
            print("Збережені нотатки у порядку їх довжини (від найкоротшої до найдовшої):")
            for note in sorted(notes, key=len, reverse=False):
                print(note.strip())
        elif command.lower() == "del":
            del_note()
        elif command.lower() == "exit":
            save_and_exit()
        else:
            print("Невідома команда. Спробуйте ще раз.")

def save_and_exit():
    """Функція виходу з програми зі збереженням нотаток"""
    quit()

if __name__ == '__main__':
    view_note()