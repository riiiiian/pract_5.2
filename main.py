from formula_1 import calculate_sh
from formula_2 import calculate_nested_ln
import utils

def main():
    """
    Основная функция программы, реализующая меню пользователя и вычисления.

    Подробное описание:
    Эта функция предоставляет пользователю интерактивное меню для выбора функций,
    ввода значений и получения результатов. Она также обрабатывает ошибки ввода
    и выводит соответствующие сообщения.

    Аргументы:
        Нет

    Возвращаемое значение:
        Нет

    Исключения:
        Нет
    """
    while True:
        print("\nМеню:")
        print("1. Вычислить sh(x)")
        print("2. Вычислить вложенный ln(x)")
        print("0. Выйти")

        try:
            choice = utils.get_int_input("Выберите пункт меню: ")
        except ValueError as e:
             print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")
             continue

        if choice == 0:
            print("Программа завершена")
            break
        elif choice == 1:
             try:
                x = utils.get_float_input("Введите значение x: ")
                result = calculate_sh(x)
                print(f"sh({x}) ≈ {result}")
             except ValueError as e:
                print(f"Ошибка при вычислении sh(x): {e}")
             except TypeError as e:
                 print(f"Ошибка при вводе: {e}")

        elif choice == 2:
            try:
                x = utils.get_float_input("Введите значение x: ")
                n = utils.get_int_input("Введите глубину вложенности (n): ")
                iterations = utils.get_int_input("Введите количество итераций (iterations) (по умолчанию 10): ") if input("Хотите ли вы изменить количество итераций? (y/n)").lower() == "y" else 10

                result = calculate_nested_ln(x, n, iterations)

                print(f"Вложенный ln(x) ≈ {result}")
            except ValueError as e:
                print(f"Ошибка при вычислении вложенного ln(x): {e}")
            except TypeError as e:
                print(f"Ошибка при вводе: {e}")

        else:
            print("Некорректный выбор. Попробуйте еще раз")


if __name__ == "__main__":
    main()