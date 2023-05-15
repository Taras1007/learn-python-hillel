# Диалог с пользователем

personal_string = input("Введите текст: ")

# Строка пользователя к нижнему регистру
lower_string = personal_string.lower()

# Удаляем со строки символы
replace_string = lower_string.replace(".", "").replace(",", "").replace("-", "")\
    .replace(":", "").replace(";", "").replace("?", "").replace("!", "")

# Удаляем лишние пробелы с правой стороны строки
right_strip_string = replace_string.rstrip(" ")

# Разделяем строку по-индексно
split_string = right_strip_string.split()

# Замена слова
question = input("Какое слово хотел бы заменить?: ")
question_lower = question.lower()

index_word = split_string.index(question_lower)
index_word_print = print("Вы выбрали слово под индексом", index_word)
answer = input("Какое слово вставить?: ")

new_sentence = right_strip_string.replace(question_lower, answer)

# Выводим результат
print("Результат:", new_sentence)