# Розраховуємо співвідношення градусів до радіан

from math import pi

degrees = float(input("Введіть значення градусів: "))   # 180 градусів == 3.14(math.pi)

radians = degrees * pi / 180

print(degrees, "градусів дорівнює", round(radians, 5), "радіан")