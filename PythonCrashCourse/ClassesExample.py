class Dog():
    """Represent a dog."""

    def __init__(self, name):
        self.name = name

    def sit(self):
        """Simulate sitting."""
        print(self.name + ' is sitting.')


class SARDog(Dog):
    """Represents a search dog"""

    def __init__(self, name):
        """Initialize the sardog"""
        super().__init__(name)

    def search(self):
        """Simulate searching."""
        print(self.name + ' is searching.')

my_dog = Dog('Peso')
print(my_dog.name + ' is a great dog!')
my_dog.sit()

my_sdog = SARDog('Willie')
print(my_sdog.name + ' is a search dog!')
my_sdog.sit()
my_sdog.search()
