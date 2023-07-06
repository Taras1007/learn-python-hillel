from .all_animals import Animals

class Cat(Animals):
    def __init__(
            self,
            name: str,
            age: int,
            say_word="Мяу-мяу"
    ):
        """
        Класс отвечает за симуляцию животного кот
        :param name: имя кота
        :param age: возраст кота
        :param say_word: что говорит кот
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"каша", "корм", "молоко"}
        )
        self.animals_type = "кот"
    def treat(self, hours: int):
        """
        После прогулки кота определенное количество времени, мы понимаем нагулялся ли кот
        :param hours: количество времени на прогулке
        :return: None
        """
        if hours > 5:
            print(f"{self.name} - {self.animals_type}, гулял сегодня {hours} часов.\nНагулялся на сегодня.")
            return ''
        else:
            print(f"{self.name} - {self.animals_type} погулял {hours} часов. Возможно еще пойдет гулять.")
            return ''
