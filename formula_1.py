import math
def calculate_sh(x, iterations=10):
    """
    Вычисляет приближенное значение гиперболического синуса sh(x) с использованием ряда Маклорена.

    Подробное описание:
    Эта функция вычисляет sh(x) путем сложения первых N членов ряда Маклорена.
    Ряд Маклорена для sh(x) выглядит так:
    sh(x) = x + x^3/3! + x^5/5! + x^7/7! + ...

    Аргументы:
        x (float): Число, для которого вычисляется гиперболический синус.
        iterations (int, optional): Количество итераций для вычисления ряда (по умолчанию 10).

    Возвращаемое значение:
        float: Приближенное значение sh(x).

    Исключения:
        TypeError: Если x не является числом или iterations не является целым числом.
        ValueError: Если iterations меньше 1.

    Примеры:
        >>> calculate_sh(0.5)
        0.5210953054937474
        >>> calculate_sh(1.0)
        1.1752011936438016
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x должен быть числом")
    if not isinstance(iterations, int):
        raise TypeError("iterations должен быть целым числом")
    if iterations < 1:
        raise ValueError("iterations должен быть не меньше 1")
    result = 0
    for i in range(iterations):
        numerator = x ** (2 * i + 1)
        denominator = math.factorial(2 * i + 1)
        result += numerator / denominator
    return result






