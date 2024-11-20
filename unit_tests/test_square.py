import unittest
from square import area, perimeter  # Assuming your square module is named square.py


class TestSquare(unittest.TestCase):
    def test_area_positive(self):
        side = 5
        self.assertEqual(area(side), 25)

    def test_perimeter_positive(self):
        side = 5
        self.assertEqual(perimeter(side), 20)

    def test_area_zero(self):
        side = 0
        self.assertEqual(area(side), 0)

    def test_perimeter_zero(self):
        side = 0
        self.assertEqual(perimeter(side), 0)

    def test_area_negative(self):
        side = -1
        with self.assertRaises(AssertionError) as context:
            area(side)
        self.assertEqual(str(context.exception), "Side cannot be negative")  

    def test_perimeter_negative(self):
        side = -1
        with self.assertRaises(AssertionError) as context:
            perimeter(side)
        self.assertEqual(str(context.exception), "Side cannot be negative")


if __name__ == '__main__':  
    unittest.main()
