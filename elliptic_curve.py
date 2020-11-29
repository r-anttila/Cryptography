from finite_field import FFieldElement


class EC(object):
    """
    An object of this class represents an algebraic elliptic curve over a finite field Z_N.
    -----------
    Parameters:
    -----------
    (int) N: The order of the field Z_N
    (int) A, B: The constants defining the elliptic curve y^2=x^3+Ax+B
    (int) x: The x coordinate of the point on the curve (the y coordinate is calculated from this one).
    """

    def __init__(self, N, A, B):
        if N == 2 or N == 3:
            raise Exception("The characteristic of the field is too small!")
        elif 4*A ^ 3+27*B ^ 2 == 0:
            raise Exception("The discriminant can not be zero!")
        else:
            self.A = FFieldElement(A, N)
            self.B = FFieldElement(B, N)
            self.N = N


class ECElement(object):
    """
    An object of this class represents a point on an algebraic elliptic curve over a finite field Z_N.
    -----------
    Parameters:
    -----------
    (EC) ec: The elliptic curve on which the point resides
    (int) x: The x coordinate of the point on the curve (the y coordinate is calculated from this one).
    """

    def __init__(self, ec, x):
        self.ec = ec
        self.x = FFieldElement(x, ec.N)
        self.ysquared = self.x.pow(3)+ec.A*self.x+ec.B
