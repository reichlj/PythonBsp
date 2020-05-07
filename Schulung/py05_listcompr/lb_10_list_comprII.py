x = [2, 4, 6, 8]
y = [3, 0, -5, 1]

print([x[i]+y[i] for i in range(4)])

first = ["lust","merci","fanci","art","power","voice"]
last = ['full','less']

print([f+l for f in first for l in last])