class Robot:
 
    def __init__(self, name="None", build_year=2000):
        self.name = name
        self.build_year = build_year 
      
    @property   
    def name(self):
        return self.__name              
    @name.setter
    def name(self, name):
        self.__name = "Marvin" if name == "Henry" else name

    @property
    def build_year(self):
        return self.__build_year
    @build_year.setter
    def build_year(self, by):
        self.__build_year = 2000 if by < 2000 else by
