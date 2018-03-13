import platform

#Set root path depending on the OS I'm working on that particular day
if platform.system()=='Windows':
    fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day9\input')
elif platform.system()=='Linux':
    fp=open('/home/user/Devel/adventofcode2017/day9/input')

level=1
score=0
garbage=False
cancel=False

while True:
    i=fp.read(1)
    if cancel:
        cancel=False
        continue
    if not i:
        break
    if i=='!':
        cancel=True
    else:
        if not garbage and i=='<':
            garbage=1
            continue
        if i=='>':
            garbage=0
        if not garbage:
            if i=='{':
                level+=1
            elif i=='}':
                level-=1
        else:
            score+=1
print score