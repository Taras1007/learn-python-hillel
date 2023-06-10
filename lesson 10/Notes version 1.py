notes = []

# Функція додавання нонатки
def add_note():
    # При виклику фуекції приймає нотатку від користувача і зберігає її в notes
    note = input("Введіть текст нотатки: ")
    notes.append(note)

# Фкнкція проходження по нотаткам
def print_notes(notes_list):
    # При виклику фуекції вона проходить по всіх нотатках і виводить на екран
    for note in notes_list:
        print(note)

# Функція роботи нотаток
def run_program():
    # При виклику функції пропонує 5 команд
    # При вибиранні певної команди користувачем виводить на екран нотатки в потрібному вигляді
    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest): ")
        # Зчитує введене значення від користувача і виводить на екран
        if command.lower() == "add":
            add_note()
        elif command.lower() == "earliest":
            print("Збережені нотатки у хронологічному порядку (від найранішої до найпізнішої):")
            print_notes(notes)
        elif command.lower() == "latest":
            print("Збережені нотатки у хронологічному порядку (від найпізнішої до найранішої):")
            print_notes(reversed(notes))
        elif command.lower() == "longest":
            print("Збережені нотатки у порядку їх довжини (від найдовшої до найкоротшої):")
            print_notes(sorted(notes, key=len, reverse=True))
        elif command.lower() == "shortest":
            print("Збережені нотатки у порядку їх довжини (від найкоротшої до найдовшої):")
            print_notes(sorted(notes, key=len, reverse=False))
        else:
            print("Невідома команда. Спробуйте ще раз.")

# Запуск програми
if __name__ == '__main__':
    run_program()