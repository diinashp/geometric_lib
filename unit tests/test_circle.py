import unittest #для написания и запуска модульных тестов
import math #для использования math.pi
import sys #для управления средой выполнения Python (в частности, добавления каталога в путь Python)
sys.path.append("..") #родительский каталог позволяет коду импортировать модуль circle

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_zero_radius(self):
        radius = 0
        predicted_area = 0
        predicted_perimeter = 0

        self.assertEqual(area(radius), predicted_area)
        self.assertEqual(perimeter(radius), predicted_perimeter)

    def test_positive_radius(self):
        radius = 1
        predicted_area = math.pi
        predicted_perimeter = 2 * math.pi

        self.assertEqual(area(radius), predicted_area)
        self.assertEqual(perimeter(radius), predicted_perimeter)

    def test_negative_radius_area(self):
        radius = -1

        with self.assertRaises(TypeError):
            area(radius)

        with self.assertRaises(TypeError):
            perimeter(radius)