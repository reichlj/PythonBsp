class C:
    counter = 0
    
    def __init__(self):
        C.counter += 1

    def __del__(self):
        C.counter -= 1
        
if __name__ == '__main__':
   x = C()
   print('Number of instances: ',str(C.counter))
   y = C()
   print('Number of instances: ',str(C.counter))
   del y
   print('Number of instances: ',str(C.counter))
   #del x
   x=9
   print('Number of instances: ',str(C.counter))

