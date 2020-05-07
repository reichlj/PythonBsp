%%file largest_files.py
#run fron terminal
import os, sys

dname = sys.argv[1] if len(sys.argv)>1 else '.'

files = os.listdir(dname)
f_list=[]
total =0
for x in files:
  fpath = dname + '/' + x
#  print(fpath,type(fpath))
  if os.path.isfile(fpath):
     hrfilesize = round(os.path.getsize(fpath) / 1024, 2)
     total += hrfilesize
     f_list.append([ x,hrfilesize])
#     print( x,hrfilesize)
f_list.sort(key=lambda x: -x[1])
print(f_list[:10])
