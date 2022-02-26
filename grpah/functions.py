import math
import numpy


class Functions:
    @staticmethod
    def f(a, b, x):
        return (a * x ** 2) / ((b + x) ** 6)

    @staticmethod
    def f_pb(a, b, x, epsilon):
        xi = numpy.random.normal(0, 1)
        return (a * x ** 2) / ((b + (epsilon * xi) + x) ** 6)

    @staticmethod
    def f_pa(a, b, x, epsilon):
        xi = numpy.random.normal(0, 1)
        return ((a + (epsilon * xi)) * x ** 2) / ((b + x) ** 6)

    @staticmethod
    def f_p(a, b, x, epsilon):
        xi = numpy.random.normal(0, 1)
        return (a * x ** 2) / ((b + x) ** 6) + (epsilon * xi)

    @staticmethod
    def lambda_(dx,  epsilon):
        if dx == 0:
            print('dx=0')
            return 0
        return math.log(dx / epsilon)

    @staticmethod
    def df(a, b, x):
        return (2 * a * x * (b - 2 * x))/((b + x) ** 7)

    @staticmethod
    def sf(a, b, x, shift):
        """Сдвиг функции f"""
        return (a * x ** 2) / ((b + x) ** 6) - shift

    @staticmethod
    def dsf(a, b, x):
        """Производная сдвига функции f"""
        return (2 * x * (b - 2 * x)) / ((b + x) ** 7)

    @staticmethod
    def g(a, x):
        return a * x

    @staticmethod
    def h(a, b, x):
        return x - (a * x ** 2) / ((b + x) ** 6)

    @staticmethod
    def dh(a, b, x):
        return (2 * a * x * (2 * x - b))/((b + x) ** 7) + 1
