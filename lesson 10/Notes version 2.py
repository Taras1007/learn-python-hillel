notebook = []
# Версія "Нотаток"
print("NOTEBOOK versoin 1.0")

# Функція головного екрану
def home_screen():
    # Функція має 4 блока які при визову переходять на відповідний інструментарій
    print("Головне меню")
    function_home_screen = input("Вибери зі списку що хочеш зробити:\n"
                                 "add - додати нотатку.\n"
                                 "del - видалити нотатку.\n"
                                 "view - щоб переглянути нотатки.\n"
                                 "quit - щоб вийти з програми.\n"
                                 "Напиши варіант сюди: ")
    # Перехід на відповідну вкладку з застосуванням некоректного вводу
    while True:
        if function_home_screen.lower() == "add":
            append_notebook()
        elif function_home_screen.lower() == "del":
            notebook_del()
        elif function_home_screen.lower() == "view":
            view_notebook()
        elif function_home_screen.lower() == "quit":
            quit_notebook()
        else:
            print("Не зрозумів вас.")
        function_home_screen = input("Повторіть ще раз.\n")

# Фуекція додавання нотаток
def append_notebook():
    # При виклику функції, вона пропонує ввести нову нотатку
    # Після чого зберігає її в notebook і повертає на головну сторінку
    us_input = input("Впиши нову нотатку:\n")
    notebook.append(us_input)
    home_screen()

# Функція видалення нотаток
def notebook_del():
    # При виклику фуекції, одразу перевіряє чи є нотатки
    # Якщо є пропонує вписати індекс і видаляє її
    if not notebook:
        print("У вас немає нотаток.")
        home_screen()

    for index, i in enumerate(notebook):
        print(f"{index}. {i}")
    quit_notebook_del = input("Якщо хочеш вийти без видалення напиши відмінити, якщо бажаєш продовжити натисни будь яку кнопку:\n")

    if quit_notebook_del.lower() == "відмінити":
        home_screen()

    else:
        # Перевірка на номер введеної нотатки і кількість всього
        # Видалення
        while True:
            index_del = input("Впиши індекс нотатки яку хочеш видалити: ")
            try:
                index_del = int(index_del)
                del notebook[index_del]
                for index, i in enumerate(notebook):
                    print(index, i)
                home_screen()
            except Exception:
                print("Не вдалося знайти нотатку.")

# Фуекція перегляду нотаток
def view_notebook():
    # При виклику фуекції одразу перевіряє чи є нотатки
    # Якщо є запитує в користувача скільки нотатків потрібно вивести на екран
    # виводить на екран потрібну кількість нотаток в обраному режимі перегляду
    if not notebook:
        print("У вас немає нотаток.")
        home_screen()

    else:
        print("Ви в вкладці перегляду блокноту.")
        numbers_note = input("Скільки нотаток бажаєте переглянути? ")
        numbers_note = int(numbers_note)
        edit_notebook = input("earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої.\n"
                              "latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої\n"
                              "longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої\n"
                              "shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої.\n"
                              "cancel - щоб повернутися до головного меню.\n"
                              "Напиши дію яку хочеш зробити:\n")

        while edit_notebook != "cancel":
            if edit_notebook.lower() == "earliest":
                for i in notebook[:numbers_note]:
                    print(i)

            elif edit_notebook.lower() == "latest":
                for i in reversed(notebook[-numbers_note:]):
                    print(i)

            elif edit_notebook.lower() == "longest":
                sorted_note = sorted(notebook[:numbers_note], key=len, reverse=True)
                for i in sorted_note:
                    print(i)

            elif edit_notebook.lower() == "shortest":
                sorted_note_1 = sorted(notebook[:numbers_note], key=len, reverse=False)
                for i in sorted_note_1:
                    print(i)

            else:
                print("Не зромів вас.")
            edit_notebook = input("Введіть варіант як ще вивести нотатки. Якщо не потрібно введіть головне меню.\n")

            if edit_notebook.lower() == "головне меню":
                home_screen()

        if edit_notebook.lower() == "cancel":
            home_screen()

# Функція виходу з програми
def quit_notebook():
    # При виклику функції програма завершує роботу
    print("До зустрічі.")
    quit()

if __name__ == '__main__':
    home_screen()