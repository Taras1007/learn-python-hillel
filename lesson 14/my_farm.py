from animals import Cat, Dog, Cow, Pig, Hen
from random import randint, choices, choice

if __name__ == '__main__':
    my_farm_animals = [
        Cat("Мурзик", 2),
        Dog("Дженифер", 3),
        Cow("Лайма", 2),
        Pig("Пеппа", 1),
        Hen("Квокча", 1)
    ]

    animals_food = ["каша", "корм", "молоко", "мясо", "суп", "сено", "трава", "вода", "овощи", "хлеб", "зерно", "пшено"]
    what_we_got = list()
    what_we_lost = list()
    for animal in my_farm_animals:
        animal.bard()
        for foods in choices(animals_food, k=3):
            what_we_lost.append(foods)
            animal.eat(foods)
        if animal.hungry:
            print(f"{animal.name} голодает, нужно покормить.")
        what_we_got.append(animal.treat(randint(0, 5)))
        animal.go_vet(choice([True, False]))
        print(f"Прошел день для {animal.name}.")
        print("=" * 20)

    print(f"Сегодня на ферме мы потратили {what_we_lost}, и получили {what_we_got}.")