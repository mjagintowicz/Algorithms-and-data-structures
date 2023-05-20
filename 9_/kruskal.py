# skonczone
import graph
import graf_mst


class UnionFind:

    def __init__(self, number_of_nodes):
        self.parent = [i for i in range(number_of_nodes)]
        self.size = [1] * number_of_nodes
        self.n = number_of_nodes

    def find(self, v):
        if self.parent[v] == v:
            return v
        else:
            return self.find(self.parent[v])

    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)
        if self.same_components(s1, s2):
            return None
        elif self.size[root1] >= self.size[root2]:
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
            return s1, s2
        else:
            self.size[root2] += self.size[root1]
            self.parent[root1] = root2
            return s2, s1

    def same_components(self, s1, s2):
        if self.find(s1) == self.find(s2):
            return True
        else:
            return False


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


def kruskal(g):
    mst_edges = []
    edges = g.edges_weights()
    edges.sort(key=lambda a: a[2])
    union = UnionFind(len(g.nodes))
    for edge in edges:
        new_edge = union.union_sets(edge[0], edge[1])
        if new_edge is not None:
            mst_edges.append(new_edge)
    mst = graph.GraphList()
    for node in list(g.nodes.keys()):
        mst.insert_vertex(node)
    for edge in mst_edges:
        ver1 = mst.get_vertex(edge[0])
        ver2 = mst.get_vertex(edge[1])
        weight = g.graph[edge[0]][edge[1]]
        mst.insert_edge(ver1, ver2, weight)
    print_graph(mst)
    return mst.edges()


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

    print_graph(test)

    edg = kruskal(test)
    print(edg)


main()
