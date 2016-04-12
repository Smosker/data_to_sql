import unittest
import tkinter
import excle


class MainTest(unittest.TestCase):
    """
    Тестирование основной фукнции программы - change_and_copy()
    """
    def setUp(self):
        root = tkinter.Tk()
        self.program = excle.Application(root)

    def test_positive(self):
        """
        Проверка на корректность преобразования данных
        """
        self.values = '123 123 123'
        self.result = "'123',\n'123',\n'123'"
        self.program.values.insert(0.0, self.values)
        self.program.change_and_copy()

        self.assertEqual(self.program.clipboard_get(), self.result)

    def test_len(self):
        """
        Проверка на корректность разбиения данных на массивы
        по 1000 значений
        """
        self.values = '123 '* 1200
        self.program.values.insert(0.0, self.values)
        self.program.change_and_copy()

        self.assertEqual(len(self.program.clipboard_get().split()), 1000)


