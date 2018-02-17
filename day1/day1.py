list="91212129"
result=[]
last=list[len(list)-1]
for i in range(0,len(list)):
    if list[i]==last:
        result+=list[i]
    last=list[i]
print sum(map(int,result))
