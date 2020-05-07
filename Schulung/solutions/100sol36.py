import sys
file_list=[
    'data/unbekannt.txt',
    'data/unbenannt.txt',
    'data/ignored.txt',
]
for fn in file_list:
    fh=None
    try:
        fh=open(fn)
    except :
        (type, value, traceback) = sys.exc_info()
        print("Type: ", type)
        print("Value: ", value)
        print("traceback: ", traceback)
        print('Failed to open '+fn+' for reading')
        print('-'*30)
        continue
    contents=fh.read()
    print(contents)
    fh.close()
        
