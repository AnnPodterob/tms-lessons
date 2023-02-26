class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __eq__(self, other: 'Rational') -> bool:
        return self.__numerator/self.__denominator == other.__numerator/other.__denominator

    def __lt__(self, other: 'Rational') -> bool:
        return self.__numerator/self.__denominator < other.__numerator/other.__denominator

    def __le__(self, other: 'Rational') -> bool:
        return self.__numerator/self.__denominator <= other.__numerator/other.__denominator

    def __ne__(self, other: 'Rational') -> bool:
        return self.__numerator/self.__denominator != other.__numerator/other.__denominator

    def __gt__(self, other: 'Rational') -> bool:
        return self.__numerator/self.__denominator > other.__numerator/other.__denominator

    def __ge__(self, other: 'Rational') -> bool:
        return self.__numerator/self.__denominator >= other.__numerator/other.__denominator

    def __normalise(self):
        if self.__denominator < 0:
            self.__numerator = -1 * self.__numerator
            self.__denominator = -1 * self.__denominator
        for i in range(min(self.numerator, self.__denominator), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                self.__numerator /= i
                self.__denominator /= i
        self.__numerator = int(self.__numerator)
        self.__denominator = int(self.__denominator)


if __name__ == '__main__':
    print(Rational(2, 4))
    print(Rational(-2, -4))
    print(Rational(2, -4))
    assert Rational(2, 4) == Rational(1, 2)
    assert Rational(1, 4) + Rational(1, 2) == Rational(3, 4)
    assert Rational(1, 2) - Rational(1, 4) == Rational(1, 4)
    assert Rational(1, 2) * Rational(2, 3) == Rational(1, 3)
    assert Rational(5, 15) / Rational(1, 3) == Rational(1, 1)
    assert Rational(2, 3) > Rational(2, 4)
    assert Rational(2, 4) < Rational(2, 3)
    assert Rational(2, 3) >= Rational(4, 6)
    assert Rational(4, 6) <= Rational(2, 3)
    frac = Rational(2, 4)
    assert frac.__mul__(Rational(2, 3)) == Rational(1, 3)

    print(Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100))
