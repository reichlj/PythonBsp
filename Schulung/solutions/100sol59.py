import os
os.environ['PYTHONPATH']=''
print('PYTHONPATH set to empty')
print('PYTHONPATH ',os.environ['PYTHONPATH'] )
#del os.environ['PYTHONPATH']
if 'PYTHONPATH' in os.environ:
    print('in if')
    print(os.environ['PYTHONPATH'] )
else:
    print('in else')
    os.environ['PYTHONPATH']=os.environ['PYTHONPATH']+os.path.pathsep+r'C:\temp\my_pthon_lib'
    print(os.environ['PYTHONPATH'] )
