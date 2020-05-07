import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

data = []
fh = open("data/hacker_poll.txt")
for line in fh:
    language, votes = line.strip().rsplit(None, 1)
    data.append((language, int(votes)))
data.sort(key=lambda x: (x[1], x[0]), reverse = True)
languages, votes = zip(*data[:10])
languages = np.asarray(languages)
votes = np.asarray(votes)
languages
total_votes = votes.sum()
total_votes
votes_percentage = votes/total_votes*100
votes_percentage
index = np.arange(len(votes))
sizes = votes_percentage
labels = languages
explode1 =[ [0]*len(votes)]  # only "explode" the 2nd slice (i.e. 'Hogs')
explode1
explode = explode1[0]
explode[0]=0.1
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
