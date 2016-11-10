# dot -Tps G.gv -o G.png


def printNDGraph(G, E):
    printed = []
    print('graph {')
    for u in G:
        for v in G[u]:
            w = G[u][v]
            if (v, u) not in printed:
                printed.append((u, v))
                if u in E and v in E[u]:
                    print(u, '--', v, '[label="' + str(w) + '",weight="' + str(w) + '",color="red"]' + ';')
                else:
                    print(u, '--', v, '[label="' + str(w) + '",weight="' + str(w) + '"]' + ';')
    print('}')


def printDGraph(G, E):
    pass
