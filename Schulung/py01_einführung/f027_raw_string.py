import os
current_path = os.getcwd()
print('-->',current_path,'<--')
path = r"C:\Users"
os.chdir(path)
new_path = os.getcwd()
print('-->',new_path,'<--')

os.chdir(current_path)
print('-->',os.getcwd(),'<--')