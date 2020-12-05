import math as m
from algebra.group import GroupElement

def shanks(g,h,ord):
    '''
    Solve the discrete logarithm problem
    g^x=h,
    where g is a generator of a cyclic group of order ord (this algorithm requires these to be known).
    Note that g and h can be instances of any subclasses of GroupElement. The method we use implements
    a naive table lookup scheme. Altering this could speed up the algorithm significantly.
    '''
    if (not isinstance(g, GroupElement) or not isinstance(h, GroupElement)):
        raise TypeError("The arguments g and h should be instances of GroupElement")
    n = m.ceil(m.sqrt(ord))
    babystep = []
    giantstep = []

    gnext = h # Save the next giantstep member in the variable gnext
    match = None # Save the possible match

    for i in range(n+1):
        babystep.append((i,g.pow(i)))
        giantstep.append((i,gnext))

        # Check for collisions in the lists (extremely inefficiently)
        for k in range(len(babystep)):
            for j in range(len(giantstep)):
                if babystep[k][1]==giantstep[j][1]:
                    match = (babystep[k][0],giantstep[j][0])
                    break
        
        gnext = gnext*g.inverse().pow(n)
    
    return (match[0]+n*match[1])%g.order


if __name__=="__main__":
    from algebra.finite_field import FFieldElement
    #Simple test problem: Solve 7^x=16 in the field Z_71. It is known that ord(7)=70

    g = FFieldElement(7,71)
    h = FFieldElement(16,71)
    ord = 70

    x = shanks(g,h,ord)
    print(x, g.pow(x))
    
