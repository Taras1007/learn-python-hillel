from .all_animals import Animals

class Pig(Animals):
    def __init__(
            self,
            name: str,
            age: int,
            say_word="Хрю-хрю"
    ):
        """
        Класс отвечает за симуляцию животного свинья
        :param name: имя свиньи
        :param age: возраст свиньи
        :param say_word: что говорит свинья
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"каша", "вода", "корм", "овощи", "хлеб"}
        )

        self.animals_type = "свинья"

    def treat(self, hours: int):
        """
        Ухаживая за свиньей отпределенное количество времени мы получаем мясо
        :param hours: сколько часов ухаживаем
        :return: 200 кг мяса или 300 кг мяса
        """
        if hours > 3:
            print(f"При ухаживании за {self.name} - {self.animals_type} {hours} часов в день, через год\n"
                  f"у нас будет 300 кг мяса.")
            return "300 кг мяса"
        else:
            print(f"Если ухаживать {hours} часов то {self.name} - {self.animals_type} большая не вырастет\n"
                  f"и будет мяса максимум 200 кг")
            return "200 кг мяса"
