import re

print(re.split(r';',"ein;zwei;drei;vier"))
print(re.split(r'\W+',"Spam, spam, spam, spam"))
print(re.split(r'\W+',"Spam, spam, spam, spam."))
print(re.split(r'(\W+)',"Spam, spam, spam, spam."))
print(re.split(r'\W+',"Spam, spam, spam, spam.",1))

line = 'surname: Obama, prename: Barack, profession: president'
print(re.split(',* *\w*: ',line))

