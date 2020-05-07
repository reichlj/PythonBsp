import sys

try:
    i = int('Hallo')
except:
    #(type,value,traceback) = sys.exc_info()
    type,value = sys.exc_info()[:2]
    print('Type: ', type)
    print('Value: ', value)
    #print('traceback: ', traceback)
    
