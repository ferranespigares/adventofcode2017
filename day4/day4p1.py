import re
valid=0
with open('C:\Users\User\Documents\dev\\adventofcode2017\day4\input') as fp:
    for line in fp:
        words=re.compile('[a-z]+').findall(line)
        tested=[]
        notvalid=False
        for word in words:
            if word not in tested:
                tested.append(word)
            else:
                notvalid=True
                break
        if not notvalid:
            valid+=1
print "Valid passphrases:",valid