def f(**args):
    print(args)
    txt = 'f('
    first = True
    for name,value in args.items():
        if not first:
            txt += ','
        else:
            first = False
        txt += "'" + str(name) + "'" + '=' + value
    txt +=')'
    print(txt)
    
f()
f(de='German',en='English')

mydict = {1:'German', 2:'English'} #TypeError: f() keywords must be strings
mydict = {'1':'German', '2':'English'}
f(**mydict)