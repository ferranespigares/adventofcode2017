f=open("input","r")
input=f.read()
f.close()
spsh=[]
for line in input.splitlines():
    spsh.append(line.split("\t"))
#convert chars to ints for entire spreadsheet using a nested list comprehension
spsh=[[int(y) for y in x] for x in spsh]
result=0
for row in spsh:
    result+=(max(row)-min(row))
print "Result:",result
 