class Clock(object):
    
    def __init__(self,h,m,s):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def tick(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                self.__hours = 0 if self.__hours == 23 else self.__hours + 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1


    def mytick(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours = 0 if self.__hours == 23 else self.__hours + 1


    def set(self,hours=0,minutes=0,seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        
    def __str__(self):
        return '{0:02d}:{1:02d}:{2:02d}'.format(self.__hours, self.__minutes, self.__seconds)
    
    def __repr__(self):
        return 'Clock('+str(self.__hours) + ',' + str(self.__minutes) +','+ str(self.__seconds) +')'
        
        
if __name__ == '__main__':
    x = Clock(23,59,30) 
    for i in range(31):
        x.tick()
        print(x) 
        print(repr(x))