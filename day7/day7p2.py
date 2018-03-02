import re, platform

def allEqual(wlist):
    if(wlist.count(wlist[0]) == len(wlist)):
        return True
    else:
        return False

def indexDifference(wlist):
        maxI=max(wlist)
        minI=min(wlist)
        if wlist.count(maxI) > wlist.count(minI):
            return wlist.index(minI)
        else:
            return wlist.index(maxI)

def children(node):
    global nodes
    children=[]
    for name,parent in nodes.items():
        if parent == node:
            children.append(name)
    return children

def siblings(node):
    global nodes
    siblings=[]
    for name,parent in nodes.items():
        if parent == nodes[node] and name != node:
            siblings.append(name)
    return siblings

def findRoot(nodes):
    for name,parent in nodes.items():
        if parent == None:
            return name

def findLeaves(nodes):
    leaves=list(nodes)
    for name,parent in nodes.items():
        if parent in leaves:
            leaves.remove(parent)
    return leaves

def treeWeight(node):
    global weights
    global subtreeWeights
    if not children(node):
        subtreeWeights[node]=weights[node]
        return weights[node]
    else:
        subtreeWeights[node]=weights[node] + sum([treeWeight(x) for x in children(node)])
        return subtreeWeights[node]

def findUnbalance(node):
    global weights
    global subtreeWeights
    global nodes
    childs=children(node)
    if not childs:
        return 0
    else:
        tw=[subtreeWeights[x] for x in childs]
        if allEqual(tw):
            return nodes[childs[0]] 
        else:
            itw=indexDifference(tw)
            return findUnbalance(childs[itw])
            

#Set root path depending on the OS I'm working on that particular day
if platform.system()=='Windows':
    fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day7\input')
elif platform.system()=='Linux':
    fp=open('/home/user/Devel/adventofcode2017/day7/sample')
      
weights={}
nodes={}
subtreeWeights={}

#Parse input file

#Build the nodes and weights lists so we have a full node list
for line in fp:
    item=filter(None,re.split('\W+',line))
    nodes[item[0]]=None
    weights[item[0]]=int(item[1])

fp.seek(0,0)

#Fill the parent relationship for each node
for line in fp:
    item=filter(None,re.split('\W+',line))
    if len(item)>2:  
        for i in range(2,len(item)):
            nodes[item[i]]=item[0]

fp.close()

#Find root node (i.e. node with no parent)
root=findRoot(nodes)
leaves=findLeaves(nodes)

#Weight the entire tree and populate weightSubtree list property for each node
treeWeight(root)
result=findUnbalance(root)
sib=siblings(result)

fixedweight=weights[result]-(subtreeWeights[result]-subtreeWeights[sib[0]])
#level=children(root)
#root_children_weight=[treeWeight(x) for x in root_children]

print "Fixed weight:",fixedweight
