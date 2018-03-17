import math


class Figure():
    def __init__(self, *args):
        self.sides = args
        self.check_correct()

    def calc_p(self):
        pass

    def name(self):
        pass

    def calc_s(self):
        pass

    def print_p_s(self):
        p = self.calc_p()
        s = self.calc_s()
        print("Периметр {} = {}, площадь = {}".format(self.name(), p, s))

    def check_correct(self):
        pass


class Triangle(Figure):
    def name(self):
        return "треугольника"

    def check_correct(self):
        p2 = self.calc_p() / 2
        for side in self.sides:
            if side >= p2:
                raise Exception("Невозможный треугольник")

    def calc_p(self):
        res = 0
        for side in self.sides:
            res += side
        return res

    def calc_s(self):
        p2 = self.calc_p() / 2
        res = p2
        for side in self.sides:
            res = res * (p2 - side)
        return math.sqrt(res)


class Rectangle(Figure):
    def name(self):
        return "прямогольника"

    def calc_p(self):
        res = 0
        for side in self.sides:
            res += side
        return res * 2

    def calc_s(self):
        res = 1
        for side in self.sides:
            res *= side
        return res


class Square(Figure):
    def name(self):
        return "квадрата"

    def calc_p(self):
        res = 0
        for side in self.sides:
            res += side
        return res * 4

    def calc_s(self):
        res = 1
        for side in self.sides:
            res *= side
        return res ** 2


class Quadrangle(Figure):
    def name(self):
        return "четырехугольника"

    def check_correct(self):
        p2 = self.calc_p() / 2
        for side in self.sides:
            if side >= p2:
                raise Exception("Невозможный четырехугольник")

    def calc_p(self):
        res = 0
        for side in self.sides:
            res += side
        return res

    def calc_s(self):
        res = 1
        p2 = self.calc_p() / 2
        res = 1
        for side in self.sides:
            res = res * (p2 - side)
        return math.sqrt(res)


def create_figure(sides):
    if len(sides) == 1:
        return Square(*sides)
    elif len(sides) == 2:
        return Rectangle(*sides)
    elif len(sides) == 3:
        return Triangle(*sides)
    elif len(sides) == 4:
        return Quadrangle(*sides)
    else:
        raise Exception("Неверное число сторон - {}".format(len(sides)))


sides = list(map(int, input("Введите стороны ").split()))
figure = create_figure(sides)
figure.print_p_s()
