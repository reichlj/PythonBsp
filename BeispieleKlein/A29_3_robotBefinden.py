import datetime
class Roboter:

    def __init__(self, name, baujahr, energie=0):
        self.name = name
        self.baujahr = baujahr
        self.energie = energie

    def alter(self):
        y = datetime.datetime.now().year
        return y - self.baujahr

    @property
    def befinden(self):
        meinalter = self.alter()
        if meinalter > 20:
            if self.energie <50:
                return "In Anbetracht meines Alters nicht so schlecht!"
            else:
                return "Super. Vor allem in Anbetracht meines Alters!"
        else:
            if self.energie < 50:
                return "Ausgelaugt!"
            else:
                return "Super!"


r = Roboter('Otto', 1990, 60)
print(r.befinden)
r = Roboter('Otto', 1990, 40)
print(r.befinden)
r = Roboter('Otto', 2010, 60)
print(r.befinden)
r = Roboter('Otto', 2010, 40)
print(r.befinden)
