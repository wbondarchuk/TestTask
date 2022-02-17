import numpy as np


def init():
    """Ввод числа и проверка его на натуральность, запуск генерации массивов и функции вывода. При ошибки-перезапуск"""
    n = int(input("Enter number:"))
    if n > 0:
        arrays = generate_arrays(n)
        print_arrays(arrays, n)
    else:
        print("Error, try again")
        init()


def random_check(num, list):
    """Проверяю на повторение размера массива, если повторяется, то надо выбрать заново и снова проверить"""
    if num not in list:
        list.append(num)
    else:
        num = np.random.randint(1, high=max_border + 1)
        random_check(num, list)
    return list


def generate_arrays(n):
    """
    Создаю n массивов
    1) Генерирую размер i-ого массива(минимальный размер выбрал 1, максимальный равен максимальному выбранному числу
    для заполнения +1, потому что randint numpy не включает верхнюю границу)
    2) Проверяю на повторение размера массива, если повторяется, то надо выбрать заново и снова проверить
    3) Генерирую числа исходя из размера (числа не проверяю на уникальность, в условии только про массивы сказано)
    4) Создаю массивы из сортированных чисел
    """
    # списки с массивами и размерами массивов
    arrays = []
    size = []
    for i in range(n):
        up = np.random.randint(1, high=max_border + 1)
        random_check(up, size)
        array = np.random.randint(min_border, high=max_border, size=size[i])
        arrays.append(sort_array(i + 1, array))
    return arrays


def sort_array(i, arr):
    """
    Сортировка: нечетные-убывание, чётные-возрастание
    Затем отсортированный массив возвращаю
    """
    if i % 2 == 0:
        arr = sorted(arr)
    else:
        arr = sorted(arr)
        arr = arr[::-1]
    return arr


def print_arrays(arrs, n):
    """
    Вывожу массивы на экран вместе с порядковым номером
    Делаю i+1, чтобы номер массива был корректный(первый будет первым, а не нулевым) и сортировка работала правильно
    Можно не делать как отдельную функцию, а включить в генерацию, но мне так удобнее)
    """
    for i in range(n):
        print(i + 1, ':', arrs[i])
        print("-----------------------")


if __name__ == '__main__':
    # Максимальное и минимальное числа, которыми заполняются массивы
    max_border = 100
    min_border = -max_border
    init()
