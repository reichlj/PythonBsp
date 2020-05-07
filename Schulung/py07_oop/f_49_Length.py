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
        if type(other) == int or type(other) == float:
            value = self.value + other/Length.__metric[self.unit]
        else:
            value = self.value + other.convert(self.unit)
        return Length(value,self.unit)

    def __iadd__(self,other):
        if type(other) == int or type(other) == float:
            self.value = self.value + other/Length.__metric[self.unit]
        else:
            self.value = self.value + other.convert(self.unit)
        return self
    
    def __str__(self):
       return str(self.value) + ' ' + self.unit

    def __repr__(self):
       return "Length(" +  str(self.value) + ",'" + self.unit + "')"


if __name__ == '__main__':
    x = Length(4,'cm')
    print(x+2)
