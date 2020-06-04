import math
import unittest


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return pow(side, 2)


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height
  

def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (diagonal_1 * diagonal_2) / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return ((base_minor * height)/2) + ((base_major*height)/2)


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (perimeter * apothem) / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    return round(math.pi * (pow(radius,2)), 2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.side = 5
            self.base = 6
            self.height = 5
            self.diagonal_1 = 5
            self.diagonal_2 = 5
            self.base_minor = 6 
            self.base_major = 8
            self.perimeter = 5
            self.apothem = 3
            self.radius = 5

        def test_square_area(self):
            # Make this test first...
            self.assertEqual(self.side**2, square_area(self.side))

        def test_rectangle_area(self):
            # Make this test first...
            self.assertEqual( 30 , rectangle_area(self.base, self.height))

        def test_triangle_area(self):
            # Make this test first...
            self.assertEqual(15, triangle_area(self.base, self.height))
        def test_rhombus_area(self):
            # Make this test first...
            self.assertEqual(12.5, rhombus_area(self.diagonal_1, self.diagonal_2))
        def test_trapezoid_area(self):
            # Make this test first...
            self.assertEqual(35, trapezoid_area(self.base_minor, self.base_major, self.height))
        def test_regular_polygon_area(self):
            # Make this test first...
            self.assertEqual(7.5, regular_polygon_area(self.perimeter, self.apothem))
        def test_circumference_area(self):
            # Make this test first...
            self.assertEqual(78.54, circumference_area(self.radius))
        def tearDown(self):
            # Delete the needed values for the tests
            pass

    unittest.main()
