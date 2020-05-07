def f():
    global s
    print(s)
    s = 'Perl'
    print(s)

    
s = 'Python'
f()
print(s)
