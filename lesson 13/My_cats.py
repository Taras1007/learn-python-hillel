from random import random, randint, choices
# Создание класса
class Cat:
    print("Создан класс Cat.")

    def __init__(self, name: str, age: int, breed: str, color: str, preferred_food: set):
        """

        :param name: имя кота
        :param age: возраст кота
        :param breed: порода кота
        :param color: цвет кота
        :param preferred_food: список еды
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.preferred_food = preferred_food
        # голодный ли кот
        self.hungry = True

    def __str__(self):
        """
        Функция строки вывода
        :return: Строка
        """
        string_cat = f"Имя: {self.name}, мой возраст - {self.age} "
        if self.age == 1:
            string_cat += "год"
        elif 1 < self.age <= 4:
            string_cat += "года"
        else:
            string_cat += "лет"
        string_cat += f", порода - {self.breed}, цвет - {self.color}"
        return string_cat

    def bark(self, count: int):
        """
        :param count: количество повторений мяукания
        """
        if count > 0:
            barking_str = '-'.join(["мяу"] * count).capitalize()
            print(f"{self.name} мяукает: {barking_str}!")

    def cat_hungry(self, food: str):
        """
        :param food: любимая еда
        :return: кушает ли кот предложенную еду
        """
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name}, кушает {food}")
            else:
                print(f"{self.name} не ест: {food}")
                self.bark(randint(1, 5))
    def out_home(self, hours: int):
        """
        :param hours: часов на прогулке
        :return: результ нагулялся ли кот
        """
        if hours > 5:
            print(f"{self.name} гуляла сегодня {hours} часов, нагулялась, хочет спать")
            return True
        else:
            print(f"{self.name}, гуляла {hours} часа, возможно еще пойдет гулять")

if __name__ == '__main__':
    a = Cat("Милка", 2, "бенгальская", "белый", {"мясо", "чай"})
    b = Cat("Джесси", 3, "британская", "черный", {"сир", "отбевна"})
    c = Cat("Жучка", 4, "ашера", "бело-черный", {"рыба", "борщ"})
    d = Cat("Сакура", 1, "свинкс", "крассный", {"каша", "молоко"})
    e = Cat("Мурзик", 1, "мейн-кун", "серый", {"корм", "сало"})
    all_cat = [a, b, c, d, e]
    potential_food = ['каша', 'молоко', 'рыба', 'борщ', 'сало', 'корм', 'яблоко', 'мясо', 'сир']
    print('Обычный день в жизни одной кошки :)')

    for cat in choices(all_cat, k=1):
        for random_food in choices(potential_food, k=3):
            cat.cat_hungry(random_food)
        hours = cat.out_home(randint(1, 10))
    print(f'Прошел день для:\n{cat}')