import re

# Створюємо функцію
def removing_brackets(string):
    # Символи по яким буде відбуватися пошук
    characters = r"\([^()]*\)"

    # Заміна збігів на порожню строку
    new_string = re.sub(characters, "", string)

    return new_string

input_text = input("Введи текст: ")

# Виклик функції
result_text = removing_brackets(input_text)

# В результаті заміна лишніх пробілів
result_text = result_text.replace("  ", " ")

# Результат
print(result_text)
