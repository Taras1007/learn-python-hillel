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
                minutes = divmod(full_seconds, 60)
                seconds = minutes[-1]                # знаходимо секунди
                hours = divmod(minutes[0], 60)
                minutes = hours[-1]                 # знаходимо хвилини
                days = divmod(hours[0], 24)
                hours = days[-1]                    # знаходимо години
                days = days[0]                      # знаходимо дні

                # зберігаємо результат в словнику
                result_time = {
                    "days": days,
                    "hours": hours,
                    "minutes": minutes,
                    "seconds": seconds,
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