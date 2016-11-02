from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 'a', 4)
makeDLinkW(C, 's', 'b', 6)
makeDLinkW(C, 's', 'c', 8)

makeDLinkW(C, 'a', 'd', 2)
makeDLinkW(C, 'a', 'b', 2)
makeDLinkW(C, 'b', 'e', 5)
makeDLinkW(C, 'b', 'f', 7)
makeDLinkW(C, 'c', 'b', 3)
makeDLinkW(C, 'c', 'f', 4)

makeDLinkW(C, 'd', 'g', 8)
makeDLinkW(C, 'd', 'e', 4)
makeDLinkW(C, 'e', 't', 6)
makeDLinkW(C, 'f', 'd', 3)
makeDLinkW(C, 'f', 'e', 3)
makeDLinkW(C, 'f', 't', 7)

makeDLinkW(C, 'g', 't', 4)

print(EdmondsKarp(C, 's', 't'))
