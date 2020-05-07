class Robot:
 
    def __init__(self, name=None, build_year=None):
        self.name = name 
        self.build_year=build_year
        
    def say_hi(self):
        Pass  # code as in previous example
            
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name    
    def set_build_year(self, by):
        self.build_year = by
        
    def get_build_year(self):
        return self.build_year    
    

x = Robot("Henry", 2008)
y = Robot()
y.set_name(x.get_name())
print(x.get_name(), x.get_build_year())
