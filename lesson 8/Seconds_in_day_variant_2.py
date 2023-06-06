def second_in_day(lover: int = 0):
    """
    Функція зчитує скільки користувач ввів секунд і переводить їх в кількість днів, годин,
    хвилин, секунд.
    lower - мінімальне значення, час не може бути відʼємним.
    """
    while True:
        try:
            # ввод від користувача
            full_seconds = int(input("Введіть кількість секунд: "))

            # перевірка на правильність вписання данних
            if lover < full_seconds:
                full_minutes = full_seconds // 60
                seconds = full_seconds - full_minutes * 60    # знаходимо секунди
                full_hours = full_minutes // 60
                minutes = full_minutes - full_hours * 60     # знаходимо хвилини
                days = full_hours // 24                    # знаходимо дні
                hours = full_hours - days * 24             # знаходимо години

                # зберігаємо результат в словнику
                result_time = {
                    "days": days,
                    "hours": hours,
                    "minutes": minutes,
                    "second": seconds,
                }
                return result_time
            else:
                print("Час не може бути відʼємним. Введи інше значення.")

        # якщо користувач ввів не коректне значення
        except Exception:
            print("Не вдалося зчитати кількість секунд, повторіть ще раз.")

# Результат
if __name__ == '__main__':
    user_seconds = second_in_day()
    print(user_seconds)