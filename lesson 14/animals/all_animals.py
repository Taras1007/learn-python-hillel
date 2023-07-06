from random import choice, randint

class Animals:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set):
        """
        Клас отвечает за симуляцию животных на ферме
        :param name: имя животного
        :param age: возраст животного
        :param say_word: что говорит животное
        :param preferred_food: любимая еда животного
        """
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self.hungry = True
        self.vet_in_year = True

    def bard(self):
        """
        Животное произносит отределенные фразы когда ей проедлагают еду которую она не ест
        """
        print(f"{self.name} говорит {self.say_word}")

    def eat(self, food: str):
        """
        Метод отвечает за симуляцию еды у животного на ферме
        Если предложенная еда есть в preferred_food, то животное наестся и self.hungry = False
        иначе животное не покушает
        :param food: что кушает
        """
        if food in self.preferred_food:
            print(f"{self.name}, кушает {food}")
            self.hungry = False
        else:
            print(f"{self.name} не ест {food}")
            self.bard()

    def treat(self, hours: int):
        """
        Метод ухаживания за животным
        :param hours: количество времени приделено ухаживанию
        :return: в зависимости от животного получаем получаем что-то определенное в замен
        """
        raise NotImplementedError

    def go_vet(self, go: bool):
        """
        Метод проверки ветеринара
        :param go: был бы ветеринар у этого животного в этом году
        :return: нужно ли обледование
        """
        if go:
            print(f"{self.name}, не был у ветеринара в этом году, нужно обследовать.")
            self.vet_in_year = True
        else:
            print(f"{self.name} в этом году обследовал ветеринар, следущее обследование через год.")
            self.vet_in_year = False
