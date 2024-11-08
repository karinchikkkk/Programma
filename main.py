def evaluate_function(function, x):
    """
    Вычисляет значение функции в точке x.

    Args:
        function (str): Строковое представление функции.
        x (float): Точка, в которой вычисляется значение функции.

    Returns:
        float: Значение функции в точке x.
    """
    # Заменяем 'x' на его значение.
    function = function.replace('x', f'({x})')
    # Пытаемся вычислить значение выражения.
    try:
        return eval(function)
    except Exception as e:
        print(f"Ошибка вычисления функции: {e}")
        return None

def derivative(function, x, h=1e-7):
    """
    Вычисляет производную функции в точке x с помощью численного метода конечных разностей.

    Args:
        function (str): Строковое представление функции.
        x (float): Точка, в которой вычисляется производная.
        h (float): Маленькое число для вычисления разности конечных.

    Returns:
        float: Значение производной в точке x.
    """
    f_x = evaluate_function(function, x)
    f_x_plus_h = evaluate_function(function, x + h)
    
    if f_x is None or f_x_plus_h is None:
        return None
    
    # Вычисляем производную через конечные разности.
    return (f_x_plus_h - f_x) / h

# Запрашиваем у пользователя строковое представление функции и точку, в которой нужно вычислить производную.
function = input("Введите строковое представление функции: ")
x_value = float(input("Введите точку, в которой нужно вычислить производную: "))

# Вычисляем производную и выводим её на экран.
result = derivative(function, x_value)
if result is not None:
    print(f"Производная функции {function} в точке {x_value} равна {result}")
else:
    print("Произошла ошибка при вычислении производной.")

input()