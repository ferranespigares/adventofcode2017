import re
fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day7\input')
weights={}
nodes={}
for line in fp:
    item=filter(None,re.split('\W+',line))
    nodes[item[0]]=None
    weights[item[0]]=item[1]

fp.seek(0,0)

for line in fp:
    item=filter(None,re.split('\W+',line))
    if len(item)>2:  
        for i in range(2,len(item)):
            nodes[item[i]]=item[0]
fp.close()

for name,parent in nodes.items():
    if parent == None:
        print "Root is:",name
        break