import math
import unittest

def uravnenie(x):
    xrad = math.radians(x)
    return  ((math.sin(xrad))/(xrad - (2 * math.cos(xrad))) + math.sqrt(((2 * math.tan(xrad))- 1)/(xrad)))

def func(x):
    try:
        result = uravnenie(x)
        print(result)
    except(ZeroDivisionError):
        print('Деление на ноль')
        result = 'Деление на ноль'
    except(TypeError):
        print('Ошибка типов данных')
        result = 'Ошибка типов данных'
    except(ValueError):
        print('Извлечение корня из отрицательного числа')
        result = 'Извлечение корня из отрицательного числа'
    except Exception as e:
        print(f"Тип ошибки: {e}")
        result = f"Тип ошибки: {e}"
    return result

'''
1 положительное + числ знач
2 отрицательное + числ знач
3 нуль - Деление на ноль
4 текст - Ошибка типов данных
5 пустой ввод - Ошибка типов данных
6 дробное + числ знач
'''
