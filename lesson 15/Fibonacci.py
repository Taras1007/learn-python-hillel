def fibonacci_numbers(number_of_repetitions: int):
    """
    Функция подсчета чисел Фибоначчи
    :param number_of_repetitions: количество чисел выведеных на экран
    """
    number_1 = 0
    number_2 = number_1 + 1
    count = 0
    while count < number_of_repetitions:
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2
        count += 1

if __name__ == '__main__':
    number_end = int(input("Сколько чисел вывести на экран?: "))
    numbers = fibonacci_numbers(number_end)

    for number in numbers:
        print(number)