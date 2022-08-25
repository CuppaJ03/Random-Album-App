## RANDOM ALBUM SELECTOR ##

import random

#picking out the albums into a list
myAlbums = []
f = open('album_list.txt','r')
for line in f:
    myAlbums.append(line.strip())
     
print('\n', random.choice(myAlbums), '\n')