print("Перевірка на паліндром")

# Ввід від користувача
user_input = input("Введи строку, для перевірки: ")

# Створив перемінну з знаками які потрібно видалити
punctuation = ',.!?-+"—«»\n'

while user_input.lower() != "стоп":
    # Видалення зайвих пробілів
    input_replace = user_input.replace(" ", "")
    # Видалення знаків "punctuation"
    for punctuation_word in punctuation:
        new_string = input_replace.replace(punctuation_word, "")
    # Приводимо строку до нижнього регістру
    new_string_lower = input_replace.lower()

    # Перевірка на паліндрома
    if new_string_lower[:] == new_string_lower[::-1]:
        print("Строка є паліндромом")
    else:
        print("Строка не є палиндромом")

    # Повторний ввід користувача
    user_input = input("Введи строку, або 'стоп', для виходу: ")

print("До зустрічі")