class Robot:
    def __init__(self,name=None,baujahr=2000):
        self.name = name
        self.baujahr = baujahr
        
    def __str__(self):
        return 'Name: ' + self.name + ' Baujahr: ' + str(self.baujahr)
    
    def __repr__(self):
        return 'Robot(name="' + self.name + '",baujahr=' + str(self.baujahr) + ')'

    def say_hi(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Hi, I am a robot without a name')
        print('Baujahr', self.baujahr)
            
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_baujahr(self, jahr):
        self.baujahr = jahr

    def get_baujahr(self):
        return self.baujahr    
        
x = Robot(baujahr=1999,name='Marvin')
print(str(x))
xstr = repr(x)
print('Rep:->',xstr,'<-')
z = eval(xstr)
print('z:',type(z))
print(z)
