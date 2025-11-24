import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def midpoint(self, other):
        return Point2D((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def midpoint(self, other):
        return Point3D((self.x + other.x) / 2, (self.y + other.y) / 2, (self.z + other.z) / 2)

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

def area_triangle(p1, p2, p3):
    a = p1.distance_to(p2)
    b = p2.distance_to(p3)
    c = p3.distance_to(p1)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_circle(radius):
    if radius < 0:
        return None
    return math.pi * radius * radius

def perimeter_circle(radius):
    if radius < 0:
        return None
    return 2 * math.pi * radius

def volume_sphere(radius):
    if radius < 0:
        return None
    return (4/3) * math.pi * radius**3

def surface_area_sphere(radius):
    if radius < 0:
        return None
    return 4 * math.pi * radius**2

def volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        return None
    return math.pi * radius**2 * height

def surface_area_cylinder(radius, height):
    if radius < 0 or height < 0:
        return None
    return (2 * math.pi * radius * height) + (2 * math.pi * radius**2)

def distance_between_points(p1, p2):
    return p1.distance_to(p2)

def is_collinear(p1, p2, p3):
    area = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    return abs(area) < 1e-9

def slope(p1, p2):
    if p1.x == p2.x:
        return float('infinity')
    return (p2.y - p1.y) / (p2.x - p1.x)

def polygon_area(points):
    n = len(points)
    if n < 3:
        return 0
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y
        area -= points[j].x * points[i].y
    return abs(area) / 2.0

class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def contains(self, point):
        return (self.top_left.x <= point.x <= self.top_left.x + self.width and
                self.top_left.y - self.height <= point.y <= self.top_left.y)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def contains(self, point):
        return self.center.distance_to(point) <= self.radius

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def slope(self):
        if self.p1.x == self.p2.x:
            return float('infinity')
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def length(self):
        return self.p1.distance_to(self.p2)

    def y_intercept(self):
        m = self.slope()
        if m == float('infinity'):
            return None
        return self.p1.y - m * self.p1.x
