fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day6\input')
input=fp.readline()
fp.close()
banks=input.split('\t')
banks=[int(i) for i in banks]
#banks=[0,2,7,0]
len=len(banks)
states=[]
count=0
while banks not in states:
    count+=1
    states.append(list(banks))
    idx=banks.index(max(banks))
    blocks=banks[idx]
    banks[idx]=0
    while blocks>0:
        idx+=1
        banks[idx%len]+=1
        blocks-=1
first_seen=states.index(banks)
print "Cycles:",count-first_seen
