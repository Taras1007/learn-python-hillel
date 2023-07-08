def string_generator(string: str):
    """
    Принимает параметр строку и выводит отдельно по слову
    :param string: сторка от пользователя
    """
    spl_string = string.split()
    for word in spl_string:
        yield word

if __name__ == '__main__':
    us_input = str(input("Введи строку: "))

    for words in string_generator(us_input):
        print(words)