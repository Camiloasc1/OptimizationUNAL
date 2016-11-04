from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 's1', 80 + 90)
makeDLinkW(C, 's', 's2', 110)

makeDLinkW(C, 's1', 'a1', 80)
makeDLinkW(C, 's1', 'b1', 90)

makeDLinkW(C, 's2', 'b1', 110)

makeDLinkW(C, 'a1', 'a2', 70)

makeDLinkW(C, 'b1', 'b2', 110)

makeDLinkW(C, 'a2', 'c', 90)

makeDLinkW(C, 'b2', 'a1', 70)
makeDLinkW(C, 'b2', 'd', 110)

makeNDLinkW(C, 'c', 'd', 20)  #
makeDLinkW(C, 'c', 't1', 90)
makeDLinkW(C, 'c', 't2', 80)

makeDLinkW(C, 'd', 't2', 70)

makeDLinkW(C, 't1', 't', 90)
makeDLinkW(C, 't2', 't', 80 + 70)

print(EdmondsKarp(C, 's', 't'))
