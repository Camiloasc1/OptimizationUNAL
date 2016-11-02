from Workshop6.Graph import *


def EdmondsKarp(C, source, sink):
    max_flow = 0
    F = {}
    R = {source: {}, sink: {}}

    for u in C:
        for v in C[u]:
            makeNDLinkW(C, u, v, 0, True)
            makeNDLinkW(F, u, v, 0)
            if C[u][v] > 0:
                makeDLinkW(R, u, v, C[u][v])

    dist, parent = BFS2(R, source)
    while dist[sink] < float('inf'):
        route = ParentRoute(parent, source, sink)
        route_capacity = min(map(lambda e: R[e[0]][e[1]], PathEdges(route)))
        max_flow += route_capacity
        for u, v in PathEdges(route):
            makeDLinkW(F, u, v, route_capacity, True)
            makeDLinkW(F, v, u, -route_capacity, True)

        R = {source: {}, sink: {}}
        for u in C:
            for v in C[u]:
                r = C[u][v] - F[u][v]
                if r > 0:
                    makeDLinkW(R, u, v, r)
        dist, parent = BFS2(R, source)

    for u in F:
        for v in F:
            if v in F[u] and F[u][v] == 0:
                del F[u][v]
            if u in F[v] and F[v][u] == 0:
                del F[v][u]
    return max_flow, F


def EdmondsKarp_Slower(C, source, sink):
    max_flow = 0
    F = {}
    R = {source: {}, sink: {}}

    for u in C:
        for v in C:
            makeDLinkW(C, u, v, 0, True)
            makeDLinkW(F, u, v, 0)
            if C[u][v] > 0:
                makeDLinkW(R, u, v, C[u][v])

    dist, parent = BFS2(R, source)
    while dist[sink] < float('inf'):
        route = ParentRoute(parent, source, sink)
        route_capacity = min(map(lambda e: R[e[0]][e[1]], PathEdges(route)))
        max_flow += route_capacity
        for u, v in PathEdges(route):
            makeDLinkW(F, u, v, route_capacity, True)
            makeDLinkW(F, v, u, -route_capacity, True)

        R = {source: {}, sink: {}}
        for u in C:
            for v in C:
                r = C[u][v] - F[u][v]
                if r > 0:
                    makeDLinkW(R, u, v, r)
        dist, parent = BFS2(R, source)

    for u in F:
        for v in F:
            if F[u][v] == 0:
                del F[u][v]
    return max_flow, F


def PathEdges(route):
    return zip(route[:-1], route[1:])
