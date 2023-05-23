# варіант перший

# список для зберігання
number = []

# 2 рази запит числа
for i in range(2):
    user_number_input = number.append(float(input("Введіть число: ")))

# цикл поки не буде введена потрібна кількість чисел
while True:
    user_input = input("Бажаєте добавити ще одне число чи вивести суму? (число/сума): ")
    if user_input.lower() == "число":
        user_input_number = number.append(float(input("Введіть число: ")))
    elif user_input.lower() == "сума":
        suma = sum(number)
        print("Відповідь:",suma)
        break
    else:
        print("Некоректний ввод. Введіть 'число' або 'сума'")