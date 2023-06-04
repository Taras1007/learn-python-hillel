def price():
    used = float(input("Витрачання палива на 100 км: "))
    price_azs = float(input("Ціна топлива: "))
    distance = float(input("Дистанція яку треба проїхати: "))

    used_fuel = used / 100 * distance   # Витрата палива

    full_price = used_fuel * price_azs    # Повна ціна
    return full_price

# Кінцевий результат
result = price()
print(f"Вам потрібно {result} грн.")