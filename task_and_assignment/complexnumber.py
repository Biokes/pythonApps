class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __lt__(self, other):
        return self.left < other.left and self.right

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __divmod__(self, other):
        return self.left / other.left and self.right / other.right

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'


object1 = Complex(2, 3)
object2 = Complex(5, -2)
print(object1)
print(object2)
print(object1 + object2)
print(object1 - object2)
print(object1 > object2)
print(object1 < object2)

