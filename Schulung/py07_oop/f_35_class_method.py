class Fraction:
    
    def __init__(self,n,d):
        self.numerator, self.denominator = type(self).reduce(n,d)

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b, a%b
        return a
            
    @classmethod
    def reduce(cls,n1,n2):
        g = cls.gcd(n1,n2)
        return ( n1//g, n2//g)
    

f = Fraction(3,24)
print(f.numerator,f.denominator)