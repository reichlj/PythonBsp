class S(object):
    __slots__ = ['val']

    def __init__(self, v):
        self.val = v

x = S(42)
print(x.val)
print(S.__slots__)
S.__slots__.append('val1')
print(S.__slots__)
y=S(142)
y.val1 =143
