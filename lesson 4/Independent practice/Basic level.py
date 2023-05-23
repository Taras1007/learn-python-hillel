# Beginner tasks

# База

# 1

number_one = float(input("Введи перше число: "))
number_two = float(input("Введи друге число: "))
if number_one > number_two:
    result = number_one - number_two
    print(number_one, "більше числа", number_two, "на", result)
else:
    result = number_two - number_one
    print(number_two, "більше числа", number_one, "на", result)

# 2

number_one = float(input("Введи перше число: "))
number_two = float(input("Введи друге число: "))
if number_one > number_two:
    result = number_one / number_two
    print(number_one, "більше числа", number_two, "у", round(result, 2), "разів")
else:
    result = number_two / number_one
    print(number_two, "більше числа", number_one, "у", round(result, 2), "разів")

# 3

number_one = float(input("Введи первше число: "))
number_two = float(input("Введи друге число: "))
if number_one > number_two:
    result = number_two * 100 / number_one
    print("Процентна ставка від", number_one, "до", number_two, "дорівнює", round(result, 2), "%")
else:
    result = number_one * 100 / number_two
    print("Процентна ставка від", number_two, "до", number_one, "дорівнює", round(result, 2), "%")

# 4

number = input("Введи число: ")
number_list = number[-1::-1]
if number == number_list:
    print("Число", number, "є паліндромом")
else:
    print("Давай друге число")

# 5

user_input = input("Введи строку: ")
user_input = user_input.capitalize()
print(user_input)

# 6

user_input = input("Введи строку: ")
user_input = user_input.title()
print(user_input)

# 7

user_input_basic = input("Введи строку: ")
user_input_one = input("Введи строку: ")
substring_input = user_input_one.lower() in user_input_basic.lower()
if substring_input == True:
    print("Строка", user_input_one, "є підстрокою строки", user_input_basic)
else:
    print("Строка", user_input_one, "не є підтрокою строки", user_input_basic)

# 8

user_input = input("Введи строку: ")
vowels = ["а", "о", "у", "е", "и", "я", "ю", "і", "є", "ї"]
vowels_list = []
for chair in user_input:
    if chair in vowels:
        vowels_list.append(chair)
print(vowels_list)