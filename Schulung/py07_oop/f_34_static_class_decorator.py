# Instance methods need a class instance and can access the instance through self.
# Class methods don’t need a class instance. They can’t access the instance (self)
#    but they have access to the class itself via cls.
# Static methods don’t have access to cls or self. They work like regular functions
#    but belong to the class’s namespace.
# Static and class methods communicate and (to a certain degree) enforce developer
#    intent about class design. This can have maintenance benefits.


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod    # indicates independent of obj and class
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.__class__.method(obj))

print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())

import math
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):  # a factory method
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):  # a factory method
        return cls(['mozzarella', 'tomatoes', 'ham'])


print(Pizza(['cheese', 'tomatoes']))
print(Pizza.margherita())
print(Pizza.prosciutto())