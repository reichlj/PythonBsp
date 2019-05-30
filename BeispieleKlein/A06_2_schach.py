sb = { ('a', 1): ('König', 'schwarz'), \
       ('a', 2): ('Bauer', 'schwarz'), \
       ('a', 7): ('Bauer', 'weiss'), \
       ('a', 8): ('Turm', 'weiss'), \
       ('b', 2): ('Bauer', 'schwarz'), \
       ('b', 7): ('Bauer', 'weiss') \
     }

print(sb[('a', 1)])
sb[('a',1)] = ('Turm', 'scharz')
print(sb[('a', 1)])
