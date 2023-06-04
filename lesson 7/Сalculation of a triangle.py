from math import sqrt

# Функція для введеня сторін
def triangle_calculation(user_input, lower_side: float = 0):
    while True:
        side = input(f"{user_input}")
        try:
            side = float(side)
            if side > lower_side:
                return side
            else:
                print("Довжина сторони не може буди мінусовим числом.")

        except Exception:
            print("Не вдалось получити данні, повторіть.")

if __name__ == '__main__':
    # Ввод довжин сторін від користувача
    a = triangle_calculation("Cторона a: ")
    b = triangle_calculation("Cторона b: ")
    c = triangle_calculation("Cторона c: ")
    print(f"Ви ввели сторони: a = {a}, b = {b}, c = {c}.")

    while True:
        # Перевірка на існування трикутника
        if a + b > c and a + c > b and b + c > a:
            print("Такий трикутник можна побудувати.")
            input_operation = input("Якщо хочеш знайти периметр напиши (периметр), ящко площу напиши (площа): ")
            # Розрахунок периметру
            if input_operation.lower() == "периметр":
                p = a + b + c
                print(f"Периметр трикутника дорівнює, {p}")
                break
            # Розрахунок площі
            elif input_operation.lower() == "площа":
                half_p = (a + b + c) / 2
                s = sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
                print(f"Площа трикутника дорівнює, {s}")
                break
        else:
            # Якщо трикутника сторони якого ввів користувач не можна побудувати, повторний запит довжин сторін
            print("Такого триугольника не можна побудувати! Введи другі данні.")
            a = triangle_calculation("Cторона a: ")
            b = triangle_calculation("Cторона b: ")
            c = triangle_calculation("Cторона c: ")
            print(f"Ви ввели сторони: a = {a}, b = {b}, c = {c}.")