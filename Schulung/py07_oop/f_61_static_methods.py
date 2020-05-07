class Pet:
    name = 'pet animals'
    
    @staticmethod
    def about():
        print('This class is about ' + Pet.name)
        
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
    Dog.about()
    