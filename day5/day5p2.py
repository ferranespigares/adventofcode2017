program=[]
fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day5\input')
for line in fp:
       program.append(int(line))
fp.close()
#program=[0,3,0,1,-3]
ip=0
count=0
while ip<len(program):
    if(program[ip]>=3):
        program[ip]-=1
        ip+=program[ip]+1
    else:
        program[ip]+=1
        ip+=program[ip]-1
    count+=1
print count