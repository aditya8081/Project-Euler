def gcd2(c,d): #this formula also gets the gcd, but does not show the steps of the Euclidean Algorithm
    if c%d == 0: # it is used for the lcm calculation later on
        return d
    return gcd2(d,(c%d))

def lcm(a,b): # this calculates the least common multiple of a and b using the gcd shown above
    return a*b/gcd2(a,b)

print lcm(lcm(lcm(lcm(lcm(lcm(lcm(lcm(lcm(lcm(2520,11),12),13),14),15),16),17),18),19),20)

# the lcm of a set of numbers can be written like this, which simplifies the math greatly
