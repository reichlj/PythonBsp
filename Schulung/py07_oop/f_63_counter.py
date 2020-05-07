class Counter(object):
    number = 0
    def __init__(self):
        type(self).number += 1
        print(type(self))
    def __del__(self):
        type(self).number -= 1
        
class A1(Counter):
     number = 0

class A2(Counter):
     number = 0

if __name__ == '__main__':
    x1 = A1()
    print(Counter.number, A1.number, A2.number)
    x2 = A1()
    print(Counter.number, A1.number, A2.number)
    c = Counter()
    y1 = A2()
    print(Counter.number, A1.number, A2.number)
    x3 = A1()
    print(Counter.number, A1.number, A2.number)
    del x1
    print(Counter.number, A1.number, A2.number)
    