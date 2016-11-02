def EdmondsKarp(C, source, sink):
    from Workshop6.Graph import makeNDLinkW, makeDLinkW, BFS2, ParentRoute
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
        route_capacity = min(map(lambda e: R[e[0]][e[1]], RouteEdges(route)))
        max_flow += route_capacity
        for u, v in RouteEdges(route):
            makeDLinkW(F, u, v, route_capacity, True)
            makeDLinkW(F, v, u, -route_capacity, True)

            makeDLinkW(R, u, v, -route_capacity, True)
            if R[u][v] <= 0:
                del R[u][v]
            makeDLinkW(R, v, u, route_capacity, True)
            if R[v][u] <= 0:
                del R[v][u]

        dist, parent = BFS2(R, source)

    for u in F:
        for v in F:
            if v in F[u] and F[u][v] == 0:
                del F[u][v]
            if u in F[v] and F[v][u] == 0:
                del F[v][u]
    return max_flow, F


# Slower
# def EdmondsKarp_2(C, source, sink):
#     from Workshop6.Graph import makeNDLinkW, makeDLinkW, BFS2, ParentRoute
#     max_flow = 0
#     F = {}
#     R = {source: {}, sink: {}}
#
#     for u in C:
#         for v in C[u]:
#             makeNDLinkW(C, u, v, 0, True)
#             makeNDLinkW(F, u, v, 0)
#             if C[u][v] > 0:
#                 makeDLinkW(R, u, v, C[u][v])
#
#     dist, parent = BFS2(R, source)
#     while dist[sink] < float('inf'):
#         route = ParentRoute(parent, source, sink)
#         route_capacity = min(map(lambda e: R[e[0]][e[1]], RouteEdges(route)))
#         max_flow += route_capacity
#         for u, v in RouteEdges(route):
#             makeDLinkW(F, u, v, route_capacity, True)
#             makeDLinkW(F, v, u, -route_capacity, True)
#
#         R = {source: {}, sink: {}}
#         for u in C:
#             for v in C[u]:
#                 r = C[u][v] - F[u][v]
#                 if r > 0:
#                     makeDLinkW(R, u, v, r)
#         dist, parent = BFS2(R, source)
#
#     for u in F:
#         for v in F:
#             if v in F[u] and F[u][v] == 0:
#                 del F[u][v]
#             if u in F[v] and F[v][u] == 0:
#                 del F[v][u]
#     return max_flow, F

# Very Slower
# def EdmondsKarp(C, source, sink):
#     from Workshop6.Graph import makeNDLinkW, makeDLinkW, BFS2, ParentRoute
#     max_flow = 0
#     F = {}
#     R = {source: {}, sink: {}}
#
#     for u in C:
#         for v in C:
#             makeDLinkW(C, u, v, 0, True)
#             makeDLinkW(F, u, v, 0)
#             if C[u][v] > 0:
#                 makeDLinkW(R, u, v, C[u][v])
#
#     dist, parent = BFS2(R, source)
#     while dist[sink] < float('inf'):
#         route = ParentRoute(parent, source, sink)
#         route_capacity = min(map(lambda e: R[e[0]][e[1]], RouteEdges(route)))
#         max_flow += route_capacity
#         for u, v in RouteEdges(route):
#             makeDLinkW(F, u, v, route_capacity, True)
#             makeDLinkW(F, v, u, -route_capacity, True)
#
#         R = {source: {}, sink: {}}
#         for u in C:
#             for v in C:
#                 r = C[u][v] - F[u][v]
#                 if r > 0:
#                     makeDLinkW(R, u, v, r)
#         dist, parent = BFS2(R, source)
#
#     for u in F:
#         for v in F:
#             if F[u][v] == 0:
#                 del F[u][v]
#     return max_flow, F


def RouteEdges(route):
    return zip(route[:-1], route[1:])
