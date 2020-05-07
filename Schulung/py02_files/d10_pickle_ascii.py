import pickle

data = (1.4, 42,'Hallo',[10,20])
output = open('data_ascii.pkl','wb')
pickle.dump(data,output,0)
output.close()

f = open('data_ascii.pkl','rb')
data = pickle.load(f)
print(data)
f.close()