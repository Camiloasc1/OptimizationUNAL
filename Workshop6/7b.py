from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 'a', 7)
makeDLinkW(C, 's', 'b', 1)
makeDLinkW(C, 's', 'c', 2)

makeDLinkW(C, 'a', 'b', 2)

makeDLinkW(C, 'b', 'a', 6)
makeDLinkW(C, 'b', 'd', 3)
makeDLinkW(C, 'b', 'e', 1)
makeDLinkW(C, 'b', 'f', 4)

makeDLinkW(C, 'c', 'b', 8)
makeDLinkW(C, 'c', 'f', 1)

makeDLinkW(C, 'd', 'e', 2)
makeDLinkW(C, 'd', 'g', 1)
makeDLinkW(C, 'd', 'h', 1)

makeDLinkW(C, 'e', 'h', 1)

makeDLinkW(C, 'f', 'e', 1)
makeDLinkW(C, 'f', 'h', 5)
makeDLinkW(C, 'f', 'i', 1)

makeDLinkW(C, 'g', 'h', 1)
makeDLinkW(C, 'g', 't', 2)

makeDLinkW(C, 'h', 't', 10)

makeDLinkW(C, 'i', 'h', 1)
makeDLinkW(C, 'i', 't', 9)

print(EdmondsKarp(C, 's', 't'))
