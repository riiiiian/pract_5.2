import math

def calculate_nested_ln(x, n, iterations=10):
    """
    Вычисляет значение вложенного натурального логарифма.

    Подробное описание:
        Эта функция вычисляет вложенный натуральный логарифм ln(1 + ln(1 + ... ln(1 + x) ... ))
        где вложенность задается параметром n.

    Аргументы:
        x (float): Значение x, для которого вычисляется логарифм. Должно быть в интервале -1 < x <= 1.
        n (int): Глубина вложенности логарифма.
        iterations (int, optional): Количество итераций для вычисления ряда (по умолчанию 10).

    Возвращает:
        float: Результат вычисления вложенного логарифма.

    Исключения:
        TypeError: Если x не является числом или n не целое число, или iterations не целое число.
        ValueError: Если x не лежит в интервале (-1, 1] или n, iterations не являются положительными целыми числами.

    Примеры:
        >>> calculate_nested_ln(0.5, 2, 3)
        0.35397376543209874
        >>> calculate_nested_ln(1.0, 1, 2)
        0.5
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x должно быть числом")
    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом")
    if not isinstance(iterations, int):
        raise TypeError("iterations должно быть целым числом")
    if iterations < 1:
        raise ValueError("iterations должно быть больше или равно 1")
    if n < 1:
        raise ValueError("n должно быть больше или равно 1")
    if not -1 < x <= 1:
         raise ValueError("x должно быть в интервале (-1, 1]")

    result = x
    for _ in range(n): # Здесь мы берем вложенность
        partial_result = 0.0
        for i in range(1, iterations + 1):
            term = ((-1) ** (i - 1)) * (result ** i) / i
            partial_result += term
        if partial_result <= 0:
            raise ValueError("Попытка взять логарифм от отрицательного числа или нуля")
        result = partial_result
    return result