fh = open('colours.txt', 'w+')
#                   1
#         0123456789012345
fh.write('The colour brown')
fh.seek(11)
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)
