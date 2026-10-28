class GeometryCalculator:
    def square(self, side):
        return side * 4, side * side

    def rectangle(self, length, width):
        return 2 * (length + width), length * width

    def circle(self, radius):
        return 2 * 3.14 * radius, 3.14 * (radius ** 2)

    def triangle(self, base, height, side_a, side_b, side_c):
        s = (side_a + side_b + side_c) / 2
        area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
        perimeter = side_a + side_b + side_c
        return perimeter, area

    def trapezoid(self, base1, base2, height, side_a, side_b):
        area = ((base1 + base2) / 2) * height
        perimeter = base1 + base2 + side_a + side_b
        return perimeter, area

    def parallelogram(self, base, height, side):
        area = base * height
        perimeter = 2 * (base + side)
        return perimeter, area

    def rhombus(self, side, d1, d2):
        area = (d1 * d2) / 2
        perimeter = 4 * side
        return perimeter, area

    def ellipse(self, a, b):
        perimeter = 2 * 3.14 * ((a2 + b2) / 2) ** 0.5
        area = 3.14 * a * b
        return perimeter, area

    def pentagon(self, side):
        area = (1/4) * (5 * (5 + 2 * (5  0.5)))  0.5 * (side ** 2)
        perimeter = 5 * side
        return perimeter, area

    def hexagon(self, side):
        area = (3 * (3  0.5) / 2) * (side  2)
        perimeter = 6 * side
        return perimeter, area

calc = GeometryCalculator()
print(calc.square(5))
print(calc.circle(3))
print(calc.hexagon(4))