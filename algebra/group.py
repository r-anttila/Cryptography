from abc import ABC, abstractmethod

class GroupElement(ABC):
    '''
    An abstract base class for an element of an algebraic group. We interpret the operation of the group as
    multiplication.
    '''
    @abstractmethod
    def __mul__(self,other):
        '''
        Multiply two GroupElement instances to get a new GroupElement.
        '''
        pass

    @abstractmethod
    def __truediv__(self,other):
        '''
        Divide self with other GroupElement. Shorthand for self*other.inverse()
        '''
        return self*other.inverse()

    @abstractmethod
    def __eq__(self,other):
        pass

    @abstractmethod
    def inverse(self):
        '''
        Find the inverse element of self in the group.
        '''
        pass

    @abstractmethod
    def pow(self, n):
        '''
        Corresponds with repeated multiplication of self n times.
        '''
        pass

class RingElement(GroupElement):
    '''
    An element of an algebraic ring. Here we exceptionally require that an instance of this
    class implements the inverse method, even though finding the inverse of the multiplicative
    monoid of the ring is not always possible. This is to ensure compatibility with the algortihms
    in the Cryptography package.
    '''

    @abstractmethod
    def __add__(self,other):
        pass

    @abstractmethod
    def __sub__(self,other):
        pass

    