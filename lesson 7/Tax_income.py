def tax_income():
    full_income = float(input("Повна сума нарахування: "))

    tax_1, tax_2 = 18, 1.5    # Відсоток податку(18% - ПДФО, 1.5% - військовий збір

    full_tax = full_income / 100 * (tax_1 + tax_2)    # Повний податок

    income = full_income - full_tax    # Чистий прибуток
    return income

# Кінцевий результат
result = tax_income()
print(f"Чистий прибуток: {result}")