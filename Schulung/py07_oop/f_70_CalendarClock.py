from f_70_clock import Clock
from f_67_Calendar import Calendar
    
class CalendarClock(Clock,Calendar):
    
    def __init__(self, day, month, year, hours=0, minutes=0, seconds=0):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)
        
    def __str__(self):
        return Calendar.__str__(self) + ', ' + Clock.__str__(self)
    
    def tick(self):
        hours_old = self._hours
        Clock.tick(self)
        if self._hours < hours_old:
            Calendar.advance(self)
            
if __name__ == '__main__':
    x = CalendarClock(31,12,57,23,59,50)
    for i in range(15):
        x.tick()
        print(x)