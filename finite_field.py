
class FField:
    """
    A helper class containing methods useful for finite field arithmetic.
    """

    @staticmethod
    def extended_euclid(a, b):
        """
        Find the unique integers x,y satisfying
        ax+by=gcd(a,b)
        Useful for finding the inverse element in a finite field by the interpretation
        ax=1 (mod b)
        """
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = divmod(b, a)
            m, n = x-u*q, y-v*q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    @staticmethod
    def check(func):
        """
        Check if the order of the fields of the elements is same when doing arithmetic operations
        """

        def wrapper(self, other):
            if(self.order == other.order):
                return func(self, other)
            else:
                raise TypeError("The elements must belong to the same field")
        return wrapper


class FFieldElement(object):
    """
    An element of a finite field.
    """

    def __init__(self, value, field_order):
        self.order = field_order
        self.value = value % self.order

    @FField.check
    def __add__(self, other):
        return FFieldElement((self.value+other.value) % self.order, self.order)

    @FField.check
    def __sub__(self, other):
        return FFieldElement((self.value-other.value) % self.order, self.order)

    @FField.check
    def __mul__(self, other):
        return FFieldElement((self.value*other.value) % self.order, self.order)

    @FField.check
    def __truediv__(self, other):
        return self * other.inverse()

    def __eq__(self, other):
        return self.value == other.value and self.order == other.order

    def inverse(self):
        gcd, x, _ = FField.extended_euclid(self.value, self.order)
        if gcd != 1:
            raise Exception("The element {} does not have an inverse element in the ring of order {}".format(
                self, self.order))
        else:
            return FFieldElement((x % self.order), self.order)

    def __repr__(self):
        return "{} (mod {})".format(self.value, self.order)

    def __str__(self):
        return str(self.value)
