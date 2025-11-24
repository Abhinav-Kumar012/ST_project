import unittest
import math
from src.geometry import (
    Point2D, Point3D, area_triangle, area_circle, perimeter_circle,
    volume_sphere, surface_area_sphere, volume_cylinder, surface_area_cylinder,
    distance_between_points, is_collinear, slope, polygon_area,
    Rectangle, Circle, Line
)

class TestPoint2D(unittest.TestCase):

    def test_distance(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(3, 4)
        self.assertEqual(p1.distance_to(p2), 5)

    def test_midpoint(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(2, 2)
        m = p1.midpoint(p2)
        self.assertEqual((m.x, m.y), (1, 1))

    def test_repr(self):
        p = Point2D(1, 2)
        self.assertEqual(repr(p), "Point2D(1, 2)")


class TestPoint3D(unittest.TestCase):

    def test_distance(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(1, 2, 2)
        self.assertEqual(p1.distance_to(p2), 3)

    def test_midpoint(self):
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(2, 2, 2)
        m = p1.midpoint(p2)
        self.assertEqual((m.x, m.y, m.z), (1, 1, 1))

    def test_repr(self):
        p = Point3D(1, 2, 3)
        self.assertEqual(repr(p), "Point3D(1, 2, 3)")


class TestGeometryFunctions(unittest.TestCase):

    def test_area_triangle(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(3, 0)
        p3 = Point2D(0, 4)
        self.assertEqual(area_triangle(p1, p2, p3), 6)

    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(3), 9 * math.pi)
        self.assertIsNone(area_circle(-1))

    def test_perimeter_circle(self):
        self.assertAlmostEqual(perimeter_circle(3), 6 * math.pi)
        self.assertIsNone(perimeter_circle(-1))

    def test_volume_sphere(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3) * math.pi)
        self.assertIsNone(volume_sphere(-1))

    def test_surface_area_sphere(self):
        self.assertEqual(surface_area_sphere(1), 4 * math.pi)
        self.assertIsNone(surface_area_sphere(-1))

    def test_volume_cylinder(self):
        self.assertEqual(volume_cylinder(1, 2), 2 * math.pi)
        self.assertIsNone(volume_cylinder(-1, 2))
        self.assertIsNone(volume_cylinder(1, -2))

    def test_surface_area_cylinder(self):
        self.assertEqual(surface_area_cylinder(1, 2),
                         2 * math.pi * 1 * 2 + 2 * math.pi * 1**2)
        self.assertIsNone(surface_area_cylinder(-1, 2))
        self.assertIsNone(surface_area_cylinder(1, -2))

    def test_distance_between_points(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(3, 4)
        self.assertEqual(distance_between_points(p1, p2), 5)

    def test_is_collinear(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(1, 1)
        p3 = Point2D(2, 2)
        self.assertTrue(is_collinear(p1, p2, p3))

        p4 = Point2D(1, 0)
        self.assertFalse(is_collinear(p1, p2, p4))

    def test_slope(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(2, 2)
        self.assertEqual(slope(p1, p2), 1)

        p3 = Point2D(0, 5)
        self.assertTrue(math.isinf(slope(p1, p3)))

    def test_polygon_area(self):
        # Square (0,0), (2,0), (2,2), (0,2)
        pts = [Point2D(0,0), Point2D(2,0), Point2D(2,2), Point2D(0,2)]
        self.assertEqual(polygon_area(pts), 4)

        # Not enough points
        self.assertEqual(polygon_area([Point2D(0,0)]), 0)


class TestRectangle(unittest.TestCase):

    def test_area(self):
        r = Rectangle(Point2D(0, 5), 4, 3)
        self.assertEqual(r.area(), 12)

    def test_perimeter(self):
        r = Rectangle(Point2D(0, 5), 4, 3)
        self.assertEqual(r.perimeter(), 14)

    def test_contains(self):
        r = Rectangle(Point2D(0, 5), 4, 3)
        inside = Point2D(2, 4)
        outside = Point2D(5, 5)
        self.assertTrue(r.contains(inside))
        self.assertFalse(r.contains(outside))


class TestCircle(unittest.TestCase):

    def test_area(self):
        c = Circle(Point2D(0,0), 2)
        self.assertEqual(c.area(), 4 * math.pi)

    def test_perimeter(self):
        c = Circle(Point2D(0,0), 2)
        self.assertEqual(c.perimeter(), 4 * math.pi)

    def test_contains(self):
        c = Circle(Point2D(0,0), 2)
        inside = Point2D(1,1)
        outside = Point2D(3,0)
        self.assertTrue(c.contains(inside))
        self.assertFalse(c.contains(outside))


class TestLine(unittest.TestCase):

    def test_slope(self):
        l = Line(Point2D(0,0), Point2D(2,2))
        self.assertEqual(l.slope(), 1)

        vertical = Line(Point2D(1,0), Point2D(1,5))
        self.assertTrue(math.isinf(vertical.slope()))

    def test_length(self):
        l = Line(Point2D(0,0), Point2D(3,4))
        self.assertEqual(l.length(), 5)

    def test_y_intercept(self):
        l = Line(Point2D(0,0), Point2D(2,2))
        self.assertEqual(l.y_intercept(), 0)

        vertical = Line(Point2D(1,0), Point2D(1,5))
        self.assertIsNone(vertical.y_intercept())


if __name__ == "__main__":
    unittest.main()
