def Prim(G):
    import heapq as Heap
    from Workshop6.Graph import makeNDLinkW
    total_cost = 0
    F = {}
    h = []

    for v in G:
        for w in G[v]:
            Heap.heappush(h, (G[v][w], v, w))
        break

    while h != []:
        d, u, v = Heap.heappop(h)
        if v in F:
            continue

        makeNDLinkW(F, u, v, d)
        total_cost += d
        for w in G[v]:
            Heap.heappush(h, (G[v][w], v, w))

    return total_cost, F
