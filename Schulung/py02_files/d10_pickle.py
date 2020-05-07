import pickle

data = (1.4, 42)
output = open('data.pkl','bw')
pickle.dump(data,output)
output.close()

f = open('data.pkl','br')
data = pickle.load(f)
print(data)
f.close()