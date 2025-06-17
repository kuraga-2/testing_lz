from testing import func
import unittest
class Test_root(unittest.TestCase):
    def test_int_pol(self):
        self.assertEqual(func(30), 0.12980642871570708)
    def test_int_neg(self):
        self.assertEqual(func(-30) , 2.250255022688834)
    def test_zero(self):
        self.assertEqual(func(0), "Деление на ноль")
    def test_zero_input(self):
        self.assertEqual(func(""),  "Ошибка типов данных")
    def test_str(self):
        self.assertEqual(func("Текст"), "Ошибка типов данных")
    def test_drob_pol(self):
        self.assertEqual(func(30.5), 0.1522351563381299)
    def test_drob_neg(self):
        self.assertEqual(func(-30.5), 2.2477972675428948)
if __name__ == "__main__":
    unittest.main()