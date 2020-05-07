fh = open('hacker_poll.txt')

data = []
for line in fh:
    language, votes = line.rsplit(' ',1)
    data.append((language,int(votes)))
data.sort(key=lambda x: (x[1],x[0]),reverse=True)

for element in data[:10]:
    print(element)
