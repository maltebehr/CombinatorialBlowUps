# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:30:53 2020

@author: behr

In this exampe, we consider R_+^3. We want to confirm that blowing up two edges
does not commute, but blowing up their intersection (the corner) afterwards
results in the first two commuting.

A mwc is representet in the following way: Given all hypersurfaces H1,...Hk,
it is representet as a subset of the powerset X\subset P(H1,...Hk)
Each Hypersurfacea is represented by its name, a string. IT IS THEREFORE
VITALLY IMPORTANT THAT ALL HYPERSURFACES HAVE A DISTINCT NAME.
Since a mwc is therefore a set of sets, it is import for python that the 
interior sets (each representing a boundary face) a so called frozensets.
"""

""" First we import the module I worte. Any function in it can the be accessed via b."""
import boundarySets as b

"""
Next we want to generate the manifold R_+^3. For this we have several otions,
which will be all presented here, which all result in the same outcome:
First of, we can type it in by hand. For this we can use the function
b.newmwc that takes a list of lists and just converts it into a set of
frozensets, as neccesary for all other functions to work.
Dont forget the empty set representing the whole manifold!
"""
triple=b.newmwc([[],['H1'],['H2'],['H3'], ['H1', 'H2'],['H1', 'H3'],['H2', 'H3'],['H1', 'H2','H3']])

"""
We can print it to check that everything worked out. The function
b.printmwc(mwc,name,depth) takes as inputs
    - the mwc
    - the name as a string, which will be just printed again to make the
      console output easyer to read
    - the depth (maximal codimension) of all bdfs that shoud be printed
      This becomes very handy for large mwcs. If it is set to 0, all bdfs
      are printed.
"""
b.printmwc(triple,"R_+^3",0)

"""
A simpler way to construct R_+^3 is to use the function b.fullmwc.
It takes a list of names of hypersurfaces and generates the manifold
where all intersections are present:
"""
triple=b.fullmwc(['H1','H2','H3'])
"""
Printing it would reveal that it is in fact the same as before.
Lastly, we may make use of the function b.power, which I would recommend.
For this we first construct the R_+:
"""
single=b.newmwc([[],['b']])
"""
And next use the function  b.power(mwc,name,k)
It creates the k-th power of mwc.
The name is a string and should represent the whole single mwc, for example 'X'.
It is used and vitally improtant, since the function b.power needs to uniquly
name all the hypersurfaces of the resulting k-th power.
Example: If mwc has a hypersufrace 'b' and the name passed to b.power is 'X',
         and the power is 3, then the resulting manifold will have
         hypersurfaces 'bXX', 'XbX', and 'XXb'
IT IS UP TO THE USER TO GUARANTEE THAT THESE RESULT IN UNIQUE NAMES
so dont call a hypersurface the same as your manifold.
"""
triple=b.power(single,'X',3)
"""
We print it again to see that it is in fact again R_+^3, however the names of
the hypersurfaces will have changed:
"""
b.printmwc(triple,'R_+^3, new way',0)

"""
We continue with the hypersurfaces namend as they are now.
Next, we want define all boundary faces that we plan to blow up.
A boundary faces needs to be tupel (surrounded by (...))where
    - The first entry is a list (or frozenset) of hypersurfaces representing
      the boundary face. It is not checked anywhere if this is in fact a
      boundary face of the manifolds you want to blow up, so you need to make
      sure of this yourself!
    - The second entry is a string which will become the name of the newly
      generated hypersurface.
"""
bbb=(["bXX", "XbX", "XXb"],"ffbbb")
bbX=(['bXX', 'XbX'],"ffbbX")
bXb=(['bXX', 'XXb'],"ffbXb")
Xbb=(['XbX', 'XXb'],"ffXbb")

"""
Next, we define the two lists of blow-ups that we want to perform.
First up, we want to check that just blowing up two edges does not commute:
"""
list1=[bbX,bXb]
list2=[bXb,bbX]
"""
Next we call the function b.iteratedBlowUp(mwc,list) which will return the
blown up space
"""
res1=b.iteratedBlowUp(triple,list1)
res2=b.iteratedBlowUp(triple,list2)

"""
Next we print the result of checking if they are equal:
"""
print('Blowing up two edgeds commutes?:')
print(res2==res1)
"""
After running this script, you may copy and paste any of the following 
commands to print out the resulting manifolds:
    b.printmwc(res1,'First Order',0)
    b.printmwc(res2,'Second Order',0)
"""

"""
Lastly, we want to check that blowing up the (lifted) corner afterwards 
results in commutativity:
"""
list3=[bbX,bXb,bbb]
list4=[bXb,bbX,bbb]

res3=b.iteratedBlowUp(triple,list3)
res4=b.iteratedBlowUp(triple,list4)

print('Blowing up two edgeds and then corner commutes?:')
print(res3==res4)
"""
Agian you might use
     b.printmwc(res3,'Third way',0)
to print out the resulting manifold.
"""