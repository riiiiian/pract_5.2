import math
def calculate_arctan(x, iterations=10):
    """
    Вычисляет приближенное значение арктангенса arctg(x) с использованием ряда Маклорена.

    Подробное описание:
    Эта функция вычисляет arctg(x) путем сложения первых N членов ряда Маклорена.
    Ряд Маклорена для arctg(x) выглядит так:
    arctg(x) = x - x^3/3 + x^5/5 - x^7/7 + ...

    Аргументы:
        x (float): Число, для которого вычисляется арктангенс.
        iterations (int, optional): Количество итераций для вычисления ряда (по умолчанию 10).

    Возвращаемое значение:
        float: Приближенное значение arctg(x).

    Исключения:
        TypeError: Если x не является числом или iterations не является целым числом.
        ValueError: Если iterations меньше 1, или x не входит в диапазон [-1, 1].

    Примеры:
        >>> calculate_arctan(0.5)
        0.4636410051781503
        >>> calculate_arctan(1.0)
        0.7853981633974483
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x должен быть числом")
    if not isinstance(iterations, int):
        raise TypeError("iterations должен быть целым числом")
    if iterations < 1:
        raise ValueError("iterations должен быть не меньше 1")
    if not -1 <= x <= 1:
        raise ValueError("x должен быть в диапазоне [-1, 1]")
    result = 0
    for i in range(iterations):
        numerator = x ** (2 * i + 1)
        denominator = 2 * i + 1
        if i % 2 == 0:
            result += numerator / denominator
        else:
            result -= numerator / denominator
    return result