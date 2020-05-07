class Length:
    
    __metric = {'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000,
                'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.344}
    
    def __init__(self, value, unit='m'):
        self.value = value
        self.unit = unit
        
    def convert(self,target_unit='m'):
        if self.unit == target_unit:
            return self.value
        else:
            return self.value*Length.__metric[self.unit]/Length.__metric[target_unit]
    
    def __add__(self,other):
        value = self.value + other.convert(self.unit)
        return Length(value,self.unit)

    def __iadd__(self,other):
        self.value = self.value + other.convert(self.unit)
        return self
    
    def __str__(self):
       return str(self.value) + ' ' + self.unit

    def __repr__(self):
       return "Length(" +  str(self.value) + ",'" + self.unit + "')"

if __name__ == '__main__':
    x = Length(4)
    print(x)
    y = Length(2.3, 'cm')
    print(x+y)
    
    z = Length(4.5, "yd") + Length(1)
    print(repr(z))
    print(z)
    
    print(Length(3,'m') + Length(2,'cm'))            
    
    print(Length(1,'m')+(Length(1,'mi')+Length(2,'cm')))     
            
    l1 = Length(3,'m')
    l1+= Length(2,'cm')
    print(l1)
    print(repr(l1))