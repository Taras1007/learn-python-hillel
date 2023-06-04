def counter():
    exponent_start = float(input("Вкажіть попередні показники лічильника: "))
    exponent_end = float(input("Вкажіть теперішні показники лічильника: "))

    used = exponent_end - exponent_start    # знаходимо кількість спожитої електроенергії за місяць
    return used

if __name__ == '__main__':
    inpt_user = counter()
    # Розрахунок в залежності від тарифу
    if inpt_user <250:
        price = inpt_user * 1.44
        print("До сплати", round(price, 2), "грн.")
    else:
        price_1 = inpt_user * 1.68
        print("До сплати", round(price_1, 2), "грн.")