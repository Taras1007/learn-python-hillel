# Розрахунок вартості спожитої електроенергії

exponent_start = float(input("Вкажіть попередні показники лічильника: "))
exponent_end = float(input("Вкажіть теперішні показники лічильника: "))

used = exponent_end - exponent_start    # знаходимо кількість спожитої електроенергії за місяць

# Розраховуємо вартість

if used <250:
    price = used * 1.44
    print("До сплати", round(price, 2), "грн.")
else:
    price_1 = used * 1.68
    print("До сплати", round(price_1, 2), "грн.")