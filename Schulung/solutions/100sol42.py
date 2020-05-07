class Clock(object):

    def __init__(self,hours=0, minutes=0, seconds=0):
        self._hours = hours     # protected, needed in ClockCalendar
        self.__minutes = minutes
        self.__seconds = seconds

    def tick(self):
        """ Time will be advanced by one second """
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                self._hours = 0 if self._hours==23  \
                                else self._hours + 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1
    def set(self,hours, minutes, seconds=0):
        self._hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return "%02d:%02d:%02d" % (self._hours, 
                                   self.__minutes, 
                                   self.__seconds)

if __name__ == "__main__":
    x = Clock(23, 59, 30)
    print(x)
    for i in range(31):
        x.tick()
    print(x)            
