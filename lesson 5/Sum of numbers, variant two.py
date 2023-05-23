# варіант другий

# список для зберінання числ
number = []

# ввод першрго числа від користувача
user_input = input("Вводь число або 'sum' для сумування: ")

# цикл допоки не буде потрібна кількість введених чисел
while user_input.lower() != 'sum':
    try:
        user_number = float(user_input)
        number.append(user_number)
    except Exception:
        print("Некоректний ввод. Введіть число або 'сума'")
    user_input = input("Вводь число або 'sum' для сумування: ")

# сумування всіх чисел введених користувачем
print("Відповідь:", sum(number))