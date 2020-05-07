import time

n = 50000

start_time = time.time()
l = []
for i in range(n):
    l = l + [i*2]
end_time = time.time()
print(end_time-start_time) 

start_time = time.time()
l = []
for i in range(n):
    l += [i*2]
end_time = time.time()
print(end_time-start_time) 

start_time = time.time()
l = []
for i in range(n):
    l.append(i*2)
end_time = time.time()
print(end_time-start_time) 
