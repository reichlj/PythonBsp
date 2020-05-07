def simple_coroutine():
    print("Koroutine wurde gestartet")
    x = yield
    print("1 Koroutine empfing: ", x)
    y = yield
    print("2 Koroutine empfing: ", y)

def simple_coroutineReturnValue():
    global x, y, z
    print("KoroutineReturn wurde gestartet",x,y)
    x = yield 42
    print("1 KoroutineReturn empfing: ", x)
    y = yield 43
    print("2 KoroutineReturn empfing: ", y)
    z = yield 44
    print("3 KoroutineReturn empfing: ", z)

x,y,z = 'x_', 'y_', 'z_'
cr = simple_coroutineReturnValue()
print('next(cr)', next(cr), x)
print("send('hi1'):", cr.send('hi1'), x)
print("send('hi2'):", cr.send('hi2'), y)
print("send('hi3'):", cr.send('hi3'), z)
#cr = simple_coroutine()
#print(cr)
#next(cr)
#cr.send('hi1')
#cr.send('hi2')

