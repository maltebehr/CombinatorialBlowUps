# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:13:39 2020

@author: behr
"""

"""
Here we check a commutativity result, that is used in the b-resolution of
the triple space in the case that the original manifold has two boundary
hypersurfaces.
"""
import boundarySets as b

single=b.newmwc([[],['H1'],['H2'],['H1','H2']])
triple=b.power(single,"X",3)
#printmwc(triple,"TripleSpace")
H222=(["H2XX","XH2X","XXH2"],"ffH222")
H111=(["H1XX","XH1X","XXH1"],"ffH111")
H22x=(["H2XX","XH2X"],"ffH22x")
H2x2=(["H2XX","XXH2"],"ffH2x2")
Hx22=(["XH2X","XXH2"],"ffHx22")
H11x=(["H1XX","XH1X"],"ffH11x")
H1x1=(["H1XX","XXH1"],"ffH1x1")
Hx11=(["XH1X","XXH1"],"ffHx11")

listofB1=[H222,H111,H22x,H2x2,Hx22,H11x,H1x1,Hx11]
listofB2=[H22x,H11x,H222,H111,H2x2,Hx22,H1x1,Hx11]

tripleRes1=b.iteratedBlowUp(triple,listofB1)
tripleRes2=b.iteratedBlowUp(triple,listofB2)

"""
The resulting manifold is only printed to depth 2
"""
b.printmwc(tripleRes1,"tripleSpace",2)

print('Does lists commute?:')
print(tripleRes1==tripleRes2)

