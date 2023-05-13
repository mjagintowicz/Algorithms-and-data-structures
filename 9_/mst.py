# skonczone

import graph
import graf_mst


def get_mst(G):
    intree = [0 for i in range(G.order())]
    distance = [float('inf') for i in range(G.order())]
    parent = [-1 for i in range(G.order())]

    weights = 0
    mst = graph.GraphList()
    vertex_stack = []
    for vertex in G.nodes.keys():
        mst.insert_vertex(vertex)
        vertex_stack.append(G.get_vertex_inx(vertex))

    v = vertex_stack[0]
    while intree[v] == 0:
        intree[v] = 1
        for n in G.neighbours(v):
            if G.graph[v][n] < distance[n] and intree[n] == 0:
                distance[n] = G.graph[v][n]
                parent[n] = v

        min_distance = distance[vertex_stack[0]]
        new_ver = vertex_stack[0]
        for ver in vertex_stack[1:]:
            if intree[ver] == 0 and min_distance > distance[ver]:
                new_ver = ver
                min_distance = distance[ver]
        if min_distance != float('inf'):
            ver1 = mst.get_vertex(new_ver)
            ver2 = mst.get_vertex(parent[new_ver])
            mst.insert_edge(ver1, ver2, min_distance)
            weights += min_distance
            v = new_ver
    return mst, weights


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours_mod(i)
        for (j, w) in nbrs:
            print(g.get_vertex(j), w, end=";")
        print()
    print("-------------------")


def main():

    test = graph.GraphList()
    for it in range(len(graf_mst.graf)):
        new_node1 = graph.Node(graf_mst.graf[it][0])
        new_node2 = graph.Node(graf_mst.graf[it][1])

        if new_node1 not in test.nodes.keys():
            test.insert_vertex(new_node1)
        if new_node2 not in test.nodes.keys():
            test.insert_vertex(new_node2)

        test.insert_edge(new_node1, new_node2, graf_mst.graf[it][2])

    mst_res = get_mst(test)
    print_graph(mst_res[0])


main()
