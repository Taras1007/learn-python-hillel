from math import pi

def calculation_radians():
    user_input = input("Введите значения градусов: ")
    degrees = float(user_input)
    radians = degrees * pi / 180    # Розрунок радіан
    return radians

# Кінцевий резудьтат
result = calculation_radians()
print(result)