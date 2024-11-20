import unittest
import sys
sys.path.append("..")

from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_sides(self):
        predicted_area = 0

        length = 0
        height = 1

        self.assertEqual(area(length, height), predicted_area)

        length = 1
        height = 0

        self.assertEqual(area(length, height), predicted_area)


        length = 0
        height = 0

        self.assertEqual(area(length, height), predicted_area)

        predicted_perimeter = 0

        side1 = 0
        side2 = 0
        side3 = 0


        self.assertEqual(perimeter(side1, side2, side3), predicted_perimeter)

    def test_positive_sides(self):
           predicted_area = 1

           length = 1
           height = 2

           self.assertEqual(area(length, height), predicted_area)

           predicted_perimeter = 3

           side1 = 1
           side2 = 1
           side3 = 1

           self.assertEqual(perimeter(side1, side2, side3), predicted_perimeter)

    def test_negative_sides(self):
            length = 1
            height = -1

            with self.assertRaises(TypeError):
                area(length, height)

            length = -1
            height = 1

            with self.assertRaises(TypeError):
                area(length, height)

            length = -1
            height = -1

            with self.assertRaises(TypeError):
                area(length, height)

            side1 = 1
            side2 = 1
            side3 = -1

            with self.assertRaises(TypeError):
                perimeter(side1, side2, side3)

            side1 = 1
            side2 = -1
            side3 = 1

            with self.assertRaises(TypeError):
                perimeter(side1, side2, side3)

            side1 = -1
            side2 = 1
            side3 = 1

            with self.assertRaises(TypeError):
                perimeter(side1, side2, side3)

            side1 = -1
            side2 = -1
            side3 = -1

            with self.assertRaises(TypeError):
                perimeter(side1, side2, side3)