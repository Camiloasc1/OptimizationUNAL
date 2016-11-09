from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 'e1', 4)
makeDLinkW(C, 's', 'e2', 4)
makeDLinkW(C, 's', 'e3', 4)
makeDLinkW(C, 's', 'e4', 4)
makeDLinkW(C, 's', 'e5', 4)
makeDLinkW(C, 's', 'e6', 4)

for e in range(1, 7):
    for p in range(1, 6):
        makeDLinkW(C, 'e' + str(e), 'p' + str(p), 1)

makeDLinkW(C, 'p1', 't', 7)
makeDLinkW(C, 'p2', 't', 6)
makeDLinkW(C, 'p3', 't', 5)
makeDLinkW(C, 'p4', 't', 4)
makeDLinkW(C, 'p5', 't', 3)
print(EdmondsKarp(C, 's', 't'))
