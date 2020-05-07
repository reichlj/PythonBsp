# %%file multithreading_sync.py
# run as: python multithreading_sync.py
import threading 
import random
import time
import datetime
lck = threading.Lock()

random.seed(42)
def incrementer(fname, id):
    time.sleep(random.random())
    global lck
    lck.acquire()
    with open(fname, 'r') as f:
        for ln in f:
            tokens = ln.split()
            n = int(tokens[0])
    n += 1
    with open(fname, 'a') as f:
        f.write(str(n)+" by " + str(id) + " at "+ datetime.datetime.now().strftime("%H:%M:%S") +'\n')

    lck.release()        
# filename to use
fname = 'counter.txt'

# re-initialize file
with open(fname, 'w') as f:
    f.write('0\n')

threads = []
for i in range(0, 20):
    t = threading.Thread(target = incrementer, args = (fname, i ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()        
