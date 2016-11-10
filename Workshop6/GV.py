# dot -Tps G.gv -o G.png


def printPrimGraph(G, E):
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


def printEdmonsKarpGraph(C, F):
    print('digraph {')
    for u in C:
        for v in C[u]:
            R = C[u][v] - F[u][v]
            if R == 0:
                print(u, '->', v,
                      '[label="' + str(F[u][v]) + '/' + str(R) + '/' + str(C[u][v]) + '",weight="' + str(
                          C[u][v]) + '",color="red"]' + ';')
            else:
                print(u, '->', v,
                      '[label="' + str(F[u][v]) + '/' + str(R) + '/' + str(C[u][v]) + '",weight="' + str(
                          C[u][v]) + '"]' + ';')
    print('}')
