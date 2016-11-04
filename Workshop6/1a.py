from Workshop6.Graph import *

C = {}
makeDLinkW(C, '1', '2', 2)
makeDLinkW(C, '1', '3', 8)

makeDLinkW(C, '2', '3', 2)
makeDLinkW(C, '2', '4', 0)

makeDLinkW(C, '3', '2', 6)
makeDLinkW(C, '3', '5', 0)

makeDLinkW(C, '4', '3', 1)
makeDLinkW(C, '4', '5', 7)
makeDLinkW(C, '4', '6', 6)

makeDLinkW(C, '5', '4', 4)
makeDLinkW(C, '5', '6', 2)

print(Dijkstra(C, '1'))
print(FloydWarshall(C))
