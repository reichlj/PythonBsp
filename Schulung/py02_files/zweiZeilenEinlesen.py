ohneEnter ='zweiZeilenOhneEnter.txt'
print("ohne Enter am Ende")
f = open(ohneEnter)
fa = []
for z in f:
    fa.append(z)
print(fa)
f.close()

f = open(ohneEnter)
print(list(fa))
f.close()

f = open(ohneEnter)
print(f.readlines())
f.close()

mitEnter ='zweiZeilenMitEnter.txt'
print("mit Enter am Ende")
f = open(mitEnter)
fa = []
for z in f:
    fa.append(z)
print(fa)
f.close()

f = open(mitEnter)
print(list(fa))
f.close()

f = open(mitEnter)
print(f.readlines())
f.close()
