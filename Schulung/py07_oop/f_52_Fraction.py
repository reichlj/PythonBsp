class Fraction:
        
    def __init__(self, z,n):
        self.__num = z
        self.__den = n
        
    def __str__(self):
       return str(self.__num) + '/' + str(self.__den)

    def __repr__(self):
       return "Fraction(" +  str(self.__num) + "," + str(self.den) + ")"

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b, a%b
        return a             

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num = self.__num // g 
        self.__den = self.__den // g 
            
    def __mul__(self,other):
        s = Fraction(self.__num*other.__num, self.__den*other.__den)
        s.reduce()
        return s

    def __div__(self,other):
        s = Fraction(self.__num*other.__den, self.__den*other.__num)
        s.reduce()
        return s

    def __truediv__(self,other):
        s = Fraction(self.__num*other.__den, self.__den*other.__num)
        s.reduce()
        return s

    def __add__(self,other):
        s = Fraction(self.__num*other.__den + self.__den*other.__num,
                     self.__den*other.__den)
        s.reduce()
        return s

    def __sub__(self,other):
        s = Fraction(self.__num*other.__den - self.__den*other.__num,
                     self.__den*other.__den)
        s.reduce()
        return s

    def __eq__(self,other):
        return self.__num*other.__den == self.__den*other.__num

    def __ne__(self,other):
        return not self.__eq__(other)

    def __gt__(self,other):
        return self.__num*other.__den > self.__den*other.__num

    def __ge__(self,other):
        return self.__num*other.__den >= self.__den*other.__num

    def __lt__(self,other):
        return self.__num*other.__den < self.__den*other.__num

    def __le__(self,other):
        return self.__num*other.__den <= self.__den*other.__num


if __name__ == '__main__':
    x = Fraction(2,6)
    y = Fraction(3,14)
    print(x*y)
    print(x/y)
    print(x + y)
    print(x - y)
    if x < y:
        print('x < y')
    else:
        print('x >= y')
        
        
    