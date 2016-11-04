from Workshop6.Graph import *
from Workshop6.Prim import Prim

C = {}
makeNDLinkW(C, '1', '2', 20)
makeNDLinkW(C, '1', '4', 35)

makeNDLinkW(C, '2', '3', 7)
makeNDLinkW(C, '2', '6', 9)

makeNDLinkW(C, '6', '3', 20)
makeNDLinkW(C, '6', '9', 4)

makeNDLinkW(C, '8', '7', 22)
makeNDLinkW(C, '8', '9', 20)

makeNDLinkW(C, '4', '7', 25)

makeNDLinkW(C, '5', '1', 30)
makeNDLinkW(C, '5', '2', 18)
makeNDLinkW(C, '5', '4', 23)
makeNDLinkW(C, '5', '6', 11)
makeNDLinkW(C, '5', '7', 12)
makeNDLinkW(C, '5', '8', 15)
makeNDLinkW(C, '5', '9', 25)

print(Prim(C))
