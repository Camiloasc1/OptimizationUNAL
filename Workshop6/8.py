from Workshop6.EdmondsKarp import *

C = {}
makeDLinkW(C, 'm1', 't1', 8)
makeDLinkW(C, 'm1', 't2', 4)
makeDLinkW(C, 'm2', 'm1', 6)
makeDLinkW(C, 'm2', 't2', 5)
makeDLinkW(C, 'm2', 't3', 6)
makeDLinkW(C, 'm3', 'm2', 8)
makeDLinkW(C, 'm3', 't3', 7)
makeDLinkW(C, 't1', 'p1', 6)
makeDLinkW(C, 't1', 'p2', 6)
makeDLinkW(C, 't1', 't2', 5)
makeDLinkW(C, 't2', 'p2', 6)
makeDLinkW(C, 't3', 't2', 5)
makeDLinkW(C, 't3', 'p2', 6)
makeDLinkW(C, 't3', 'p3', 6)
makeDLinkW(C, 'p2', 'p1', 6)
makeDLinkW(C, 'p2', 'p3', 6)

makeDLinkW(C, 'p1', 't', 5)
makeDLinkW(C, 'p2', 't', 10)
makeDLinkW(C, 'p3', 't', 15)

makeDLinkW(C, 's', 'm1', 14)
makeDLinkW(C, 's', 'm2', 9)
makeDLinkW(C, 's', 'm3', 7)
print(EdmondsKarp(C, 's', 't'))
