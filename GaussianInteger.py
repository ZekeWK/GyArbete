import math

class GaussianInteger:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def new(tuple):
        return GaussianInteger(tuple[0], tuple[1])
    
    def __str__(self):
        if self.b >= 0:
            return str(self.a) + " + " + str(self.b) + "i"
        else:
            return str(self.a) + " - " + str(-self.b) + "i"

    def __abs__(self):
        return int(math.sqrt(self.a**2 + self.a**2))
    
    def abs2(self):
        return self.a**2 + self.b**2

    def con(self):
        return GaussianInteger(self.a, -self.b)

    def real(self):
        return self.a

    def imag(self):
        return self.b

    def __add__(self, other):
        return GaussianInteger(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return GaussianInteger(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        if type(other) == GaussianInteger:
            return GaussianInteger(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
        else:
            return GaussianInteger(self.a * other, self.b * other)
    __rmul__ = __mul__

    def __floordiv__(self, other):
        if type(other) == GaussianInteger:
            return (self * other.con()) // other.abs2()
        else:
            return GaussianInteger(self.a / other, self.b / other)

    def get_tuple(self):
        return (self.a, self.b)