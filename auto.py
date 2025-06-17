from testing import func
import unittest
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