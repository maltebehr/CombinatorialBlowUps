# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:13:02 2020
@author: behr
For examples see test files.
"""
from itertools import chain, combinations #is just needed for the function fullmwc

"""
Takes a list of lists representing boundary faces and converts it into to correct type
"""
def newmwc(faces):
    return set(map(frozenset,faces))

"""
Takes a list of bhs and creates a mwc whith all intersections present.
"""
def fullmwc(bhs):
    s = list(bhs)
    return set(map(frozenset,chain.from_iterable(combinations(s, r) for r in range(len(s)+1))))

"""
blowup takes a manifold s as a set of frozensets, a element b of s
(as a frozen set) and a string ff as a name for the new front face
For convenience, bdf may be a list, not a frozenset
"""
def blowup(mwc,bdf,ffname):
    fbdf=frozenset(bdf) # Since bdf may still be a list, not frozenset
    subb={x for x in mwc if fbdf.issubset(x)}# all bdfs that are a part of fbdf
    connb={x for x in mwc.difference(subb) if (frozenset(fbdf.union(x)) in subb)}
        #connb= all bdfs that are NOT in fbdf but have a common section
    newfaces={frozenset(x.union({ffname})) for x in connb}
        #generating the new bdfs resulting from blow-up
    return (mwc.difference(subb)).union(newfaces)#old minus subb plus newfaces

"""
Printing out a mwc somewhat nicer
It prints out all bdfs up to codimension depth
If depth=0 it prints out all bdfs.
"""
def printmwc(mwc,name,depth):
    m=[list(x) for x in mwc]
    maxdepth=max([len(x) for x in m])
    if (depth==0):
        depth= maxdepth
    print("Printing "+name+". Maximal codimension: " +str(maxdepth))
    print("Number of boundary faces in total: "+str(len(m)))
    temp=[[] for i in range(0,depth)]
    for bdf in m:
        if len(bdf)<=depth and bdf!=[]:
            temp[len(bdf)-1].append(bdf)
    for i in range(0,depth):
        print("Codim "+str(i+1)+"("+str(len(temp[i]))+" total):"+str(temp[i]))

"""
A list of bdf that are going to be blown up is a list of tuples where
    -the first entrie is a bdf (either frozenset or list)
    -the second item is a Name for the new front face
This function lifts such a list under the blow-up of a single bdf.
This is nessecary since the list might contain bdfs
that are sub-bdfs of the bdf that is blown up.
"""
def liftListOfbdfs(listofbdf,blownupbdf,ff,blownupmwc):
    lift=list()
    for x in listofbdf:
        if frozenset(x[0]) in blownupmwc:
            lift.append(x)
        else:
            temp=set(x[0])
            temp.difference_update(set(blownupbdf))
            temp.update({ff})
            lift.append((temp,x[1]))
    return lift
            
"""
This function blows up all the bdf in listOfBlowUps. It is basically just 
recursion.
"""
def iteratedBlowUp(mwc,listOfbdfs):
    if listOfbdfs==[]:
        return mwc
    else:
        bdf=listOfbdfs.pop(0)
        bumwc=blowup(mwc,bdf[0],bdf[1])
        return iteratedBlowUp(bumwc,liftListOfbdfs(listOfbdfs,bdf[0],bdf[1],bumwc))

"""
retunrs the product of mwc1 and mwc2 ans a mwc.
The names are relevant for the naming of the bdfs.
"""
def product(mwc1,name1,mwc2,name2):
    prod=set()
    for x in mwc1:
        for y in mwc2:
            temp=set()
            for xx in x:
                newel=xx+name2
                temp.update({newel})
            for yy in y:
                newel=name1+yy
                temp.update({newel})
            prod.add(frozenset(temp))
    return prod

"""
Returns the k-th power of mwc with itself.
"""
def power(mwc,name,k):
    po=mwc
    name2=name
    for i in range(2,k+1):
        po=product(po,name2,mwc,name)
        name2=name2+name
    return po
