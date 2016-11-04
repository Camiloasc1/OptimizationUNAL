from Workshop6.Graph import *
from Workshop6.EdmondsKarp import EdmondsKarp

C = {}
makeDLinkW(C, 's', 'p1', 600)
makeDLinkW(C, 's', 'p2', 500)
makeDLinkW(C, 's', 'p3', 500)

makeDLinkW(C, 'p1', 'a', 400)
makeDLinkW(C, 'p1', 'c', 300)

makeDLinkW(C, 'p2', 'c', 500)

makeDLinkW(C, 'p3', 'c', 200)
makeDLinkW(C, 'p3', 'e', 200)

makeDLinkW(C, 'a', 'b', 300)

makeDLinkW(C, 'b', 't', 600)

makeDLinkW(C, 'c', 'a', 100)
makeDLinkW(C, 'c', 'd', 600)
makeDLinkW(C, 'c', 'e', 200)

makeDLinkW(C, 'd', 'b', 200)
makeDLinkW(C, 'd', 't', 400)

makeDLinkW(C, 'e', 'd', 300)
makeDLinkW(C, 'e', 't', 300)

print(EdmondsKarp(C, 's', 't'))
