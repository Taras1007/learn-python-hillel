from .all_animals import Animals

class Hen(Animals):
    def __init__(
            self,
            name: str,
            age: int,
            say_word="Ко-ко"
    ):
        """
        Класс отвечает за симуляцию животного курица
        :param name: имя курицы
        :param age: возраст курицы
        :param say_word: что говорит курица
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"зерно", "пшено", "вода"}
        )
        self.animals_type = "курица"

    def treat(self, hours: int):
        """
        Ухаживая за курицей упределенное количетво времени мы получаем яйца
        :param hours: сколько часов ухаживаем
        :return: 10 или 5 яиц
        """
        if hours > 2:
            print(f"Если ухаживать за {self.name} - {self.animals_type} {hours} часов, она будет давать 10 яиц в день.")
            return "10 яиц"
        else:
            print(f"Если ухаживать за {self.name} - {self.animals_type} {hours} часов в день, то будет давать 5 яиц.")
            return "5 яиц"