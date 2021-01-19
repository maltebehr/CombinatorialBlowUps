# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:04:20 2020

@author: behr
"""

"""
Here the main example is given. It is exactly as in our notes.
"""
import boundarySets as b

single=b.newmwc([[],["H1"],["H2"],["H1","H2"]])
triple=b.power(single,"X",3)
#printmwc(triple,"TripleSpace")
H222=(["H2XX","XH2X","XXH2"],"ffH222")
H221=(["H2XX","XH2X","XXH1"],"ffH221")
H212=(["H2XX","XH1X","XXH2"],"ffH212")
H122=(["H1XX","XH2X","XXH2"],"ffH122")
H211=(["H2XX","XH1X","XXH1"],"ffH211")
H121=(["H1XX","XH2X","XXH1"],"ffH121")
H112=(["H1XX","XH1X","XXH2"],"ffH112")
H111=(["H1XX","XH1X","XXH1"],"ffH111")
H22x=(["H2XX","XH2X"],"ffH22x")
H2x2=(["H2XX","XXH2"],"ffH2x2")
Hx22=(["XH2X","XXH2"],"ffHx22")
H21x=(["H2XX","XH1X"],"ffH21x")
H2x1=(["H2XX","XXH1"],"ffH2x1")
Hx21=(["XH2X","XXH1"],"ffHx21")
H12x=(["H1XX","XH2X"],"ffH12x")
H1x2=(["H1XX","XXH2"],"ffH1x2")
Hx12=(["XH1X","XXH2"],"ffHx12")
H11x=(["H1XX","XH1X"],"ffH11x")
H1x1=(["H1XX","XXH1"],"ffH1x1")
Hx11=(["XH1X","XXH1"],"ffHx11")

listofB1=[H222,H221,H212,H122,H211,H121,H112,H111,H22x,H2x2,Hx22,H21x,H2x1,Hx21,H12x,H1x2,Hx12,H11x,H1x1,Hx11]
listofB2=[H22x,H21x,H12x,H11x,H222,H221,H212,H122,H211,H121,H112,H111,H2x2,Hx22,H2x1,Hx21,H1x2,Hx12,H1x1,Hx11]



tripleRes1=b.iteratedBlowUp(triple,listofB1)
tripleRes2=b.iteratedBlowUp(triple,listofB2)

b.printmwc(tripleRes1,'Res1',1)

print('Lists commute?:')
print(tripleRes1==tripleRes2)
