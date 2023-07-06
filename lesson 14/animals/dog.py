from .all_animals import Animals

class Dog(Animals):
    def __init__(
            self,
            name: str,
            age: int,
            say_word="Гав-гав"
    ):
        """
        Класс отвечает за симуляцию животного собака
        :param name: имя соабки
        :param age: возраст собаки
        :param say_word: что говорит собака
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"мясо", "суп", "каша"}
        )
        self.animals_type = "собака"
    def treat(self, hours: int):
        """
        Гуляя с собакой определенное количество времени, мы получаем хорошее настроение
        :param hours: количество времени на прогулке
        :return: хорошее настроение или ничего
        """
        if hours > 5:
            print(f"После {hours} часовой прогулки с , {self.name} - {self.animals_type} вернулись счастливыми.")
            return "Хорошее настроение"
        else:
            print(f"После того как мы с {self.name} - {self.animals_type} погуляли\n"
                  f"{hours} часов, вернулись, но пойдем еще.")
            return ''