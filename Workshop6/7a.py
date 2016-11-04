from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 'a', 3)
makeDLinkW(C, 's', 'b', 4)
makeDLinkW(C, 's', 'd', 1)

makeDLinkW(C, 'a', 'e', 4)

makeDLinkW(C, 'b', 'c', 1)
makeDLinkW(C, 'b', 'e', 2)
makeDLinkW(C, 'b', 'f', 1)

makeDLinkW(C, 'c', 'f', 2)

makeDLinkW(C, 'd', 'c', 3)
makeDLinkW(C, 'd', 'f', 2)

makeDLinkW(C, 'e', 't', 5)

makeDLinkW(C, 'f', 't', 6)

print(EdmondsKarp(C, 's', 't'))
