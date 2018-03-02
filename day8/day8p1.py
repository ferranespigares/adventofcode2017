import platform

def doOps(instruction,oper1,value):
    global registers
    if instruction == 'inc':
        registers[oper1]+=int(value)
    else:
        registers[oper1]-=int(value)

#Set root path depending on the OS I'm working on that particular day
if platform.system()=='Windows':
    fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day8\input')
elif platform.system()=='Linux':
    fp=open('/home/user/Devel/adventofcode2017/day8/sample')

instructions=[]
registers={}
absolutemax=0
for line in fp:
    instructions.append(line.split())

for ins in instructions:
    if ins[0] not in registers:
        registers[ins[0]]=0
#    if ins[4] not in registers:
#        registers.append(ins[4])

for ins in instructions:
    if ins[5] == '<':
        if registers[ins[4]] < int(ins[6]):
            doOps(ins[1],ins[0],ins[2])
    elif ins[5] == '>':
        if registers[ins[4]] > int(ins[6]):
            doOps(ins[1],ins[0],ins[2])
    elif ins[5] == '==':
        if registers[ins[4]] == int(ins[6]):
            doOps(ins[1],ins[0],ins[2])
    elif ins[5] == '>=':
        if registers[ins[4]] >= int(ins[6]):
            doOps(ins[1],ins[0],ins[2])
    elif ins[5] == '<=':
        if registers[ins[4]] <= int(ins[6]):
            doOps(ins[1],ins[0],ins[2])
    elif ins[5] == '!=':
        if registers[ins[4]] != int(ins[6]):
            doOps(ins[1],ins[0],ins[2])

print "There are %s registers" % len(registers)
print "Largest register value:",max(registers.values())
