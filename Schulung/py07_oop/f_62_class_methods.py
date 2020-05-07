class Pet:
    name = 'pet animals'
    
    @classmethod
    def about(cls):
        print(cls.__name__)
        print('This class is about ' + cls.name)
        
class Dog(Pet):
    name = 'dogs'

class Cat(Pet):
    name = 'cats'
    

if __name__ == '__main__':
    p = Pet()
    p.about()
    Pet.about()
    d = Dog()
    d.about()
    c = Cat()
    c.about()
    Cat.about()
