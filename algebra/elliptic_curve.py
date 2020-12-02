from finite_field import FFieldElement
from group import GroupElement

class ECExeption(Exception):
    def __init__(self,e):
        super().__init__(e)

class EC:
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


class ECElement(GroupElement):
    """
    An object of this class represents a point on an algebraic elliptic curve over a finite field Z_N.
    -----------
    Parameters:
    -----------
    (EC) ec: The elliptic curve on which the point resides
    (int) x: The x coordinate of the point on the curve (the y coordinate is calculated from this one).
    """
    ec, x, A, B, N, y = None, None, None, None, None, None

    def __init__(self, ec, x, y):
        self.ec = ec
        if x != None and y != None:
            self.x = FFieldElement(x, ec.N)
            self.A = ec.A
            self.B = ec.B
            self.N = ec.N
            self.y = FFieldElement(y,ec.N)
            self.isunit = False
            if self.y.pow(2) != self.x.pow(3)+self.A*self.x+self.B:
                raise ValueError("The point (x,y) is not on the curve!")

    @classmethod
    def from_x(cls,ec,x):
        fx = FFieldElement(x,ec.N)
        return cls(ec,x,cls._get_y(fx.pow(3)+ec.A*fx+ec.B,ec.N))

    @classmethod
    def unit(cls,ec):
        unit = cls(ec, None, None)
        unit.isunit = True
        return unit
     
    @staticmethod
    def _get_y(ysquared,N):
        # We get the value of y from y squared naively by calculating x^2 for every x in the finite field
        # and checking if x^2=y^2. This can be improved dramatically by e.g. using the Tonelli-Shanks algorithm.
        for i in range(N):
            i = FFieldElement(i,N)
            if (i.pow(2)==ysquared):
                return i.value
        raise ECExeption("No element of the curve corresponds to this value of x!")

    def __mul__(self,other):
        if self.isunit :
            return other
        elif other.isunit:
            return self
        elif self.isinverse(other):
            return ECElement.unit(self.ec)
        elif self == other:
            if self.y==FFieldElement(0,self.N):
                return ECElement.unit(self.ec)
            else:
                lamb = (FFieldElement(3,self.N)*self.x.pow(2)+self.A)/(FFieldElement(2,self.N)*self.y)
        else:
            lamb=(other.y-self.y)/(other.x-self.x)

        x = lamb.pow(2)-self.x-other.x
        y = lamb*(self.x-x)-self.y

        return ECElement(self.ec,x.value,y.value)

    def __truediv__(self,other):
        return self*other.inverse()

    def __eq__(self,other):
        if self.isunit and other.isunit:
            return True
        else:
            return self.x==other.x and self.y==other.y and self.ec==other.ec

    def inverse(self):
        return ECElement(self.ec,self.x.value,-self.y.value)
    
    def isinverse(self,other):
        return self.inverse() == other

    def pow(self,n):
        '''
        Raise the element to the power n using the fast powering algorithm
        '''
        n = bin(n)[::-1]
        result = ECElement.unit(self.ec)
        Q = self

        for i in n:
            if i=="b":
                break
            elif int(i)==1:
                result = result*Q
            Q = Q*Q

        return result


    def __repr__(self):
        if self.isunit:
            return "UNIT, E({}):x^3+{}x+{}".format(self.N,self.A,self.B)
        else:
            return "({},{}), E({}):x^3+{}x+{}".format(self.x,self.y,self.N,self.A,self.B)
    
    def __str__(self):
        if self.isunit:
            return "UNIT"
        else:
            return "({},{})".format(self.x,self.y)
            
if __name__=="__main__":
    ec = EC(5,1,4)
    e = ECElement(ec,0,2)

    print(e.pow(7))