class Calendar(object):
    
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    
    def __init__(self, day=1, month=1, year=1900):
        self.__day__ = day
        self.__month__ = month
        self.__year__ = year
        
    @staticmethod
    def leap_year(year):
        if year % 4 :
            return 0
        else:
            if year % 100:
                return 1
            else:
                return 0 if year % 400 else 1 

    def set(self,day,month,year):
        self.__day__ = day
        self.__month__ = month
        self.__year__ = year

    def get(self):
        return self.__day__, self.__month__, self.__year__
    
    def advance(self):
        days = Calendar.months[self.__month__-1]
        if self.__month__ == 2:
            days += Calendar.leap_year(self.___year__)
        if self.__day__ == days:
           self.__day__ = 1
           if self.__month__ == 12:
               self.__month__ = 1
               self.__year__ += 1
           else:
               self.month +=1
        else:
            self.__day__ +=1
            
    def __str__(self):
        return str(self.__day__) + '/' + str(self.__month__) + '/' + str(self.__year__)
                
        
if __name__ == '__main__'        :
    x = Calendar()
    print(x)
    x.advance()
    print(x)
    
