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
    row.sort(reverse=True)
    for j in range(0,len(row)-1):
        for i in range(j+1,len(row)):
            if row[j]%row[i]==0:
                result+=(row[j]/row[i])
print "Result:",result
 