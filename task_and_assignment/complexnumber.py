class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __lt__(self, other):
        return self.left < other.left and self.right < other.right

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __truediv__(self, other):
        return Complex(self.left / other.left, self.right / other.right)

    def __mul__(self, other):
        return Complex(self.left * other.left, self.right * other.right)

    def __floordiv__(self, other):
        return self.left / other.left and self.right / other.right

    def __iadd__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __idiv__(self, other):
        return Complex(self.left / other.left, self.right / other.right)

    def __isub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __pow__(self, power):
        return Complex(self.left ** power.left, self.right ** power.right)

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'


if __name__ == '__main__':
    object1 = Complex(2, 3)
    object2 = Complex(5, -2)
    # object1 **= object2
    print(object1, " pow")
    print(object1 + object2, "plus")
    print(object1 - object2, "minus")
    print(object1 / object2, "div")
    print(object1 < object2, "greater than")
    print(object1 * object2, "multiply")
    print(object1 > object2, "lesser than")
    object1 /= object2
    print(object1, '*=')
    object1 -= object2
    print(object1, " -=")
    object1 += object2
    print(object1, " +=")
    object1 /= object2
    print(object1, " /=")
    object1 //= object2
    print(object1, "//=")
    constant = ((2 * 50 * 100) / 30) ** 0.5


def formulae(num):
    return ((2 * 50 * num) / 30) ** (1 / 2)


def constants(*args):
    value = ''
    count = 0
    for numbers in list(args):
        value += f"{int(formulae(numbers)):.0f}"
        if count == len(list(args)) - 1:
            value += ""
        else:
            value += ","
        count += 1

    return value


print(constants(100, 150, 180))
