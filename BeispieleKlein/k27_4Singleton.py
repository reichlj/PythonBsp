class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        print(Singleton._instances)
        return cls._instances[cls]

class SingletonClass(metaclass=Singleton):
    pass

class MySingletonClass(metaclass=Singleton):
    pass

class RegularClass:
    pass

x = SingletonClass()
y = SingletonClass()
print(x == y, id(x), id(y))

x = MySingletonClass()
y = MySingletonClass()
print(x == y, id(x), id(y))

x = RegularClass()
y = RegularClass()
print(x==y,id(x),id(y))
