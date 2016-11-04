from Workshop6.Graph import *
from Workshop6.Prim import Prim

C = {}
makeNDLinkW(C, '1', '2', 14)
makeNDLinkW(C, '1', '3', 5)
makeNDLinkW(C, '1', '4', 2)

makeNDLinkW(C, '2', '3', 9)
makeNDLinkW(C, '2', '4', 8)

makeNDLinkW(C, '3', '6', 8)

makeNDLinkW(C, '4', '8', 11)

makeNDLinkW(C, '5', '2', 15)
makeNDLinkW(C, '5', '3', 13)
makeNDLinkW(C, '5', '4', 10)
makeNDLinkW(C, '5', '6', 1)
makeNDLinkW(C, '5', '7', 7)
makeNDLinkW(C, '5', '8', 5)

makeNDLinkW(C, '7', '6', 10)
makeNDLinkW(C, '7', '8', 0)

makeNDLinkW(C, '9', '6', 11)
makeNDLinkW(C, '9', '7', 12)
makeNDLinkW(C, '9', '8', 6)

print(Prim(C))
