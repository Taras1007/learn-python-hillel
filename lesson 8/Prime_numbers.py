def prime_numbers(number_min: int = 0, number_max: int = 100):
    """
    Функція перевіряє чи є введене число простим.
    Створено список по якому буде відбуватися пошук, якщо введене число цикл for знайде в заданих
    то повертвє True, якщо ні то поверне False."""
    """
    number_min - мінімальне число яке може перевірити програма.
    number_max - максимальне число яке може перевірити програма.
    """
    # Список простих чисел від 0 до 100
    numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    used_number = input("Введи число від 1 (включно) до 100, щоб перевірити чи воно просте: ")
    while True:
        try:
            used_number = int(used_number)
            # Перевірка на вимогу функції
            if number_min < used_number <= number_max:
                if used_number in numbers:
                    return True
                else:
                    return False
            else:
                print("Число повинно бути в діапазоні між 0 і 100.")
                used_number = input("Введи число від 0 до 100 щоб перевірити чи воно просте: ")

        # Якщо не коректний ввод
        except Exception:
            print("Не вдалось получити число, повторіть спробу.")
            used_number = input("Введи число від 0 до 100 щоб перевірити чи воно просте: ")

# Результат
if __name__ == '__main__':
    user_input = prime_numbers()
    print(user_input)
