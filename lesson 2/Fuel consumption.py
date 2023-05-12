# Розраховуємо ціну на топливо

used = float(input("Витрачання палива на 100 км: "))
price = float(input("Ціна топлива: "))
distance = float(input("Дистанція яку треба проїхати: "))

used_fuel = used / 100 * distance   # Витрата палива

full_price = used_fuel * price    # Повна ціна

print("Знадобиться", round(full_price, 2), "грн для того щоб проїхати", distance, "км.")