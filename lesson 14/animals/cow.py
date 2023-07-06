from .all_animals import Animals

class Cow(Animals):
    def __init__(
            self,
            name: str,
            age: int,
            say_word="Му-му"
    ):
        """
        Класс отвечает за симуляцию животного корова
        :param name: имя коровы
        :param age: возраст коровы
        :param say_word: что говорит корова
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"сено", "трава", "вода"}
        )
        self.animals_type = "корова"

    def treat(self, hours: int):
        """
        Ухаживая за коровой определенное количество времени мы получаем молоко
        :param hours: сколько часов ухаживаем
        :return: молоко или ничего
        """
        if hours > 2:
            print(f"Если ухаживать за {self.name} - {self.animals_type} {hours} часов в день, то она будет давать молоко")
            return "Ведро молока"
        else:
            print(f"Если ухаживать за {self.name} - {self.animals_type} {hours}, молока сегодня не будет")
            return ''