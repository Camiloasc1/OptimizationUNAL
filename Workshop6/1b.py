from Workshop6.Graph import *

C = {}
makeDLinkW(C, '1', '4', 10)
makeDLinkW(C, '1', '2', 5)

makeDLinkW(C, '2', '5', 1)
makeDLinkW(C, '2', '3', 7)

makeDLinkW(C, '3', '6', 4)

makeDLinkW(C, '4', '7', 11)
makeDLinkW(C, '4', '5', 3)

makeDLinkW(C, '5', '8', 7)
makeDLinkW(C, '5', '6', 3)

makeDLinkW(C, '6', '9', 5)

makeDLinkW(C, '7', '10', 9)
makeDLinkW(C, '7', '8', 2)

makeDLinkW(C, '8', '11', 1)
makeDLinkW(C, '8', '9', 0)

makeDLinkW(C, '9', '12', 12)

makeDLinkW(C, '10', '11', 2)

makeDLinkW(C, '11', '12', 4)

print(Dijkstra(C, '1'))
print(FloydWarshall(C))
