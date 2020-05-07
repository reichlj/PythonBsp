import os, subprocess
fn= input('Dateipfad bitte: ')
print('your input: ', fn)
!type bundeslaender.txt
#x = subprocess.Popen(['type ' + fn]) # not under W10
x = subprocess.Popen('type ' + fn, shell=True)
print(x.returncode)
print(subprocess.getoutput('type %s'%fn))
