from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 'a', 1)
makeDLinkW(C, 's', 'b', 1)
makeDLinkW(C, 's', 'c', 1)
makeDLinkW(C, 's', 'd', 1)
makeDLinkW(C, 's', 'f', 1)

makeDLinkW(C, 'a', 'b', 1)
makeDLinkW(C, 'a', 'd', 1)

makeDLinkW(C, 'b', 'd', 1)
makeDLinkW(C, 'b', 'e', 1)
makeDLinkW(C, 'b', 'f', 1)

makeDLinkW(C, 'c', 'b', 1)
makeDLinkW(C, 'c', 'e', 1)
makeDLinkW(C, 'c', 'f', 1)

makeDLinkW(C, 'd', 'g', 1)
makeDLinkW(C, 'd', 't', 1)
makeDLinkW(C, 'd', 'h', 1)

makeDLinkW(C, 'e', 'd', 1)
makeNDLinkW(C, 'e', 'f', 1)  #
makeDLinkW(C, 'e', 'h', 1)

makeDLinkW(C, 'f', 'h', 1)
makeDLinkW(C, 'f', 'i', 1)
makeDLinkW(C, 'f', 't', 1)

makeDLinkW(C, 'g', 't', 1)

makeDLinkW(C, 'h', 'g', 1)
makeDLinkW(C, 'h', 'i', 1)
makeDLinkW(C, 'h', 't', 1)

makeDLinkW(C, 'i', 't', 1)

print(EdmondsKarp(C, 's', 't'))
