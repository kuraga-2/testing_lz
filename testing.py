import math
import unittest

def uravnenie(x):
    xrad = math.radians(x)
    
    result = ((math.sin(xrad))/(xrad - (2 * math.cos(xrad))) + math.sqrt(((2 * math.tan(xrad))- xrad)/(xrad)))
    return result
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


class Test_root(unittest.TestCase):
    def test_int_pol(self):
        self.assertEqual(func(30), 0.6841161949584038)
    def test_int_neg(self):
        self.assertEqual(func(-30) , 1.3195342903601486)
    def test_zero(self):
        self.assertEqual(func(0), "Деление на ноль")
    def test_zero_input(self):
        self.assertEqual(func(""), "Ошибка типов данных")
    def test_str(self):
        self.assertEqual(func("Текст"), "Ошибка типов данных")
    def test_drob_pol(self):
        self.assertEqual(func(30.5), 0.6752400052387378)
    def test_drob_neg(self):
        self.assertEqual(func(-30.5), 1.3264229330631874)
if __name__ == "__main__":
    unittest.main()
func()

'''
1 положительное
2 отрицательное
3 нуль
4 текст
5 пустой ввод
6 дробное
'''
