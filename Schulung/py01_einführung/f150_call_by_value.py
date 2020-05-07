def ref_demo(x):
    print('ref_demo x=',x, 'id=',id(x))
    x = 42
    print('ref_demo x=',x, 'id=',id(x))

x=9
print('main x=',x,'id=',id(x))
ref_demo(x)
print('main x=',x,'id=',id(x))

x=42
print('main x=',x,'id=',id(x))
ref_demo(x)
print('main x=',x,'id=',id(x))
