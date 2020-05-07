import re
t = "A fat cat doesn't eat oat but a rat eats bat."
mo = re.findall("[force]at",t)
print(mo)

iterator = re.finditer("[force]at",t)
for k in iterator:
    print(k.group(), end=' ')