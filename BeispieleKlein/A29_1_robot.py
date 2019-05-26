class Robot:
    def __init__(self,name):
        if name == "Hugo":
            self.name = "Marvin"
        else:
            self.name = name


# Lösung mit Properties
class Robot1:

    def __init__(self, name):
         self.name = name

    def _set_name(self, name):
        if name == "Hugo":
            self.__name = "Marvin"
        else:
            self.__name = name

    def _get_name(self):
        return self.__name
    name = property(_get_name, _set_name)


class Robot2:
    """Lösung mit Property-Decorator"""

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "Hugo":
            self.__name = "Marvin"
        else:
            self.__name = name

class Robot3:
    """Lösung mit Property-Decorator"""

    def __init__(self, name):
        self.name1 = name

    @property
    def name(self):
        return self.name1

    @name.setter
    def name(self, name):
        if name == "Hugo":
            self.name1 = "Marvin"
        else:
            self.name1 = name


x=Robot("Marvin")
y=Robot("Hugo")
print(x.name, y.name)
print(x.__dict__)

x=Robot1("Marvin")
y=Robot1("Hugo")
print(x.name,y.name)
print(x.__dict__)

x=Robot2("Marvin")
y=Robot2("Hugo")
print(x.name,y.name)
print(x.__dict__)

x=Robot3("Marvin")
y=Robot3("Hugo")
print(x.name,y.name)
print(x.__dict__)
