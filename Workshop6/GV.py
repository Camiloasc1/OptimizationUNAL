# dot -Tpng G.gv -o G.png
import os

file_number = 0


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
    global file_number
    file_number += 1
    with open('img/' + str(file_number) + '.gv', 'w') as file:
        file.write('digraph {' + '\n')
        for u in C:
            for v in C[u]:
                R = C[u][v] - F[u][v]
                if R == 0 and C[u][v] != 0:
                    file.write(u + ' -> ' + v + ' [label="' + str(F[u][v]) + '/' + str(R) + '/' + str(
                        C[u][v]) + '",weight="' + str(C[u][v]) + '",color="red"]' + ';' + '\n')
                else:
                    file.write(u + ' -> ' + v + ' [label="' + str(F[u][v]) + '/' + str(R) + '/' + str(
                        C[u][v]) + '",weight="' + str(C[u][v]) + '"]' + ';' + '\n')
        file.write('}' + '\n')
    os.system('dot -Tpng img/' + str(file_number) + '.gv -o img/' + str(file_number) + '.png')
