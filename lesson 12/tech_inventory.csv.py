import csv


def reading_file(file_name):
    """
    Функція для зчитування файлу

    :param file_name: назва файлу

    :return: список товарів
    """
    list_file = []
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_file.append(row)
    return list_file


def unit_id(list_file):
    """
    Функція створення унікальних id

    :param list_file: список товарів

    :return: словник з унікальними id
    """
    dikt_ids = {}
    for item in list_file:
        ids = hash(frozenset(item.items()))
        dikt_ids[ids] = item
    return dikt_ids


def category_index(list_file):
    """
    Функція створення індексу по категоріям

    :param list_file: список товарів

    :return: словник з категоріями
    """
    tech_category_index = {}
    for item in list_file:
        category = item["category"]
        ids = hash(frozenset(item.items()))
        if category not in tech_category_index:
            tech_category_index[category] = []
        tech_category_index[category].append(ids)
    return tech_category_index


def brand_index(list_file):
    """
    Функція створення індексу по брендам

    :param list_file: список товарів

    :return: словник з брендами
    """
    tech_brand_index = {}
    for item in list_file:
        brand = item["brand"]
        ids = hash(frozenset(item.items()))
        if brand not in tech_brand_index:
            tech_brand_index[brand] = []
        tech_brand_index[brand].append(ids)
    return tech_brand_index


def print_brand(list_file):
    """
    Функція виводу інформації за брендами

    :param list_file: список товарів

    """
    dict_brand = {}
    for item in list_file:
        brand = item["brand"]
        if brand not in dict_brand:
            dict_brand[brand] = 0
        dict_brand[brand] += 1

    print("Вивід на екран інформацію за брендами:")
    for brand, count in dict_brand.items():
        print(f"{brand}: {count} товарів.")


def print_category(list_file):
    """
    Функція виводу інформації за категоріями

    :param list_file: список товарів
    """
    dict_category = {}
    for item in list_file:
        category = item["category"]
        if category not in dict_category:
            dict_category[category] = 0
        dict_category[category] += 1

    print("Вивід на екран інформацію за категорією:")
    for category, count in dict_category.items():
        print(f"{category}: {count} товарів.")


def item_by_brand(inventory, brand, category):
    """
    Функція віводу товару за обраним брендом
    :param inventory: список товарів
    :param brand: обраний бренд
    :param category: обрана категорія
    """
    print(f"Вивід на екран бренду {brand} в категорії {category}")
    for item in inventory:
        if item["brand"] == brand and item["category"] == category:
            print(item)


def calculate_brand_by_category(inventory):
    """
    Фуекція для підрахунку товарів по брендам для кожної категорії

    :param inventory: список товарів

    :return: словник розподілених товарів
    """
    dick_brand_in_category = {}
    for item in inventory:
        brand = item["brand"]
        category = item["category"]
        if category not in dick_brand_in_category:
            dick_brand_in_category[category] = {}
        if brand not in dick_brand_in_category[category]:
            dick_brand_in_category[category][brand] = 0
        dick_brand_in_category[category][brand] += 1
    return dick_brand_in_category


def print_calculate(dick_brand_in_category):
    """
    Функція виведення розподілених товарів

    :param dick_brand_in_category: словник з розподіленими товарами
    """
    print("Розподіл товарів за брендом та категоріями:")
    for category, brands in dick_brand_in_category.items():
        print(category)
        for brand, count in brands.items():
            print(f"{brand}: {count} товарів.")


if __name__ == '__main__':
    my_inventory = reading_file("tech_inventory.csv")
    ids_inventory = unit_id(my_inventory)
    category = category_index(my_inventory)
    brand = brand_index(my_inventory)
    print_brends = print_brand(my_inventory)
    print_categoryes = print_category(my_inventory)
    name_brand = str(input("Введи назву бренду: "))
    category_brand = str(input("Введи назву категорії: "))
    print_brends_and_category = item_by_brand(my_inventory, name_brand, category_brand)
    calculates_with_brand = calculate_brand_by_category(my_inventory)
    print_calculate_with_brand = print_calculate(calculates_with_brand)
