class Pet:
    name = 'pet animals'
    
    def about(self):
        print(type(self))
        print('   This class is about ' + self.name)
        if issubclass(type(self), (Dog,Cat)):
             print('   Super name:', super(type(self), self).name)

class Dog(Pet):
    name = 'dogs'

class Cat(Pet):
    name = 'cats'
    

if __name__ == '__main__':
    p = Pet()
    p.about()
    d = Dog()
    d.about()
    c = Cat()
    c.about()
    print('Super name of Cat:', super(Cat, c).name)
    print(dir(c))
    print(dir(Pet))
    print(dir(Cat))
