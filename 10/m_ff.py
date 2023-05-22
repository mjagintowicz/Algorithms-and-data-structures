# skonczone
class Node:

    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if type(other) == Node:
            return self.key == other.key
        else:
            return self.key == other

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)


class GraphList:

    def __init__(self):
        self.graph = []
        self.nodes = {}

        self.graph_res = []

    def is_empty(self):
        if not self.nodes:
            return True
        else:
            return False

    def insert_vertex(self, vertex):
        self.nodes[vertex] = self.order()
        self.graph.append({})
        self.graph_res.append({})

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.nodes.keys() and vertex2 in self.nodes.keys():
            inx1 = self.get_vertex_inx(vertex1)
            inx2 = self.get_vertex_inx(vertex2)
            self.graph[inx1][inx2] = edge

    def insert_edge_res(self, vertex1, vertex2, edge=None):
        if vertex1 in self.nodes.keys() and vertex2 in self.nodes.keys():
            inx1 = self.get_vertex_inx(vertex1)
            inx2 = self.get_vertex_inx(vertex2)
            self.graph_res[inx1][inx2] = edge

    def delete_vertex(self, vertex):
        if vertex in self.nodes.keys():
            inx = self.get_vertex_inx(vertex)
            for i in range(self.order()):
                for key in self.graph[i].keys():
                    if key == inx:
                        del self.graph[i][key]
                        break
            for i in range(self.order()):
                for key in self.graph_res[i].keys():
                    if key == inx:
                        del self.graph_res[i][key]
                        break
            self.graph.pop(inx)
            self.graph_res.pop(inx)
            self.nodes.pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.nodes.keys() and vertex2 in self.nodes.keys():
            inx1 = self.get_vertex_inx(vertex1)
            inx2 = self.get_vertex_inx(vertex2)
            if inx2 in list(self.graph[inx1].keys()):
                del self.graph[inx1][inx2]
            if inx1 in list(self.graph[inx2].keys()):
                del self.graph[inx2][inx1]

    def delete_edge_res(self, vertex1, vertex2):
        if vertex1 in self.nodes.keys() and vertex2 in self.nodes.keys():
            inx1 = self.get_vertex_inx(vertex1)
            inx2 = self.get_vertex_inx(vertex2)
            if inx2 in list(self.graph_res[inx1].keys()):
                del self.graph_res[inx1][inx2]
            if inx1 in list(self.graph_res[inx2].keys()):
                del self.graph_res[inx2][inx1]

    def get_vertex_inx(self, vertex):
        return self.nodes[vertex]

    def get_vertex(self, vertex_inx):
        pos = list(self.nodes.values()).index(vertex_inx)
        return list(self.nodes.keys())[pos]

    def neighbours(self, vertex_inx):
        return list(self.graph[vertex_inx].keys())

    def neighbours_mod(self, vertex_inx):
        n = list(self.graph[vertex_inx].keys())
        w = list(self.graph[vertex_inx].values())
        result = []
        for i in range(len(n)):
            result.append((n[i], w[i]))
        return result

    def order(self):
        return len(self.nodes)

    def size(self):
        return len(self.graph)

    def edges(self):
        edg = []
        for i in range(self.order()):
            for k in list(self.graph[i].keys()):
                edg.append((self.get_vertex(i), self.get_vertex(k)))
        return edg


class Edge:

    def __init__(self, capacity, isResidual):
        self.capacity = capacity
        self.flow = 0
        self.isResidual = isResidual
        if isResidual is False:
            self.residual = capacity
        else:
            self.residual = 0

    def __repr__(self):
        s = 'cap: '
        s += '{}'.format(self.capacity)
        s += ', flow: '
        s += '{}'.format(self.flow)
        s += ', res: '
        s += '{}'.format(self.residual)
        s += ', '
        s += '{}'.format(self.isResidual)
        return s


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours_mod(i)
        for (j, w) in nbrs:
            print(g.get_vertex(j), w, end="; ")
        print()
    print("-------------------")


def bfs(g):
    visited = [0]*len(g.nodes)
    parent = [-1]*len(g.nodes)
    queue = []
    visited[0] = 1
    queue.append(0)
    while queue:
        v = queue.pop(0)
        for n in g.neighbours(v):
            if visited[n] == 0 and g.graph[v][n].residual > 0:
                queue.append(n)
                visited[n] = 1
                parent[n] = v
    return parent


def find_capacity(g, start, stop, parent):
    inx = stop
    min_cap = float('inf')
    if parent[stop] == -1:
        return 0
    else:
        while inx != start:
            edge = g.graph[parent[inx]][inx]
            if edge.residual < min_cap:
                min_cap = edge.residual
            inx = parent[inx]
    return min_cap


def path(g, start, stop, parent, min_cap):
    inx = stop
    while inx != start:
        edge = g.graph[parent[inx]][inx]
        edge.flow += min_cap
        edge.residual -= min_cap
        edge_res = g.graph_res[inx][parent[inx]]
        edge_res.residual += min_cap
        inx = parent[inx]


def ff_ek(g, start, stop):
    parent = bfs(g)
    min_cap = find_capacity(g, start, stop, parent)
    while min_cap > 0:
        path(g, start, stop, parent, min_cap)
        parent = bfs(g)
        min_cap = find_capacity(g, start, stop, parent)
    flow = 0
    for i in range(len(g.graph)):
        for n in g.neighbours(i):
            if n == stop:
                flow += g.graph[i][n].flow
    return flow


def graph_from_tuples(list_of_tuples):
    new_graph = GraphList()
    for data in list_of_tuples:
        ver1 = Node(data[0])
        ver2 = Node(data[1])
        if data[0] not in new_graph.nodes.keys():
            new_graph.insert_vertex(ver1)
        if data[1] not in new_graph.nodes.keys():
            new_graph.insert_vertex(ver2)
        new_edge = Edge(data[2], False)
        new_edge_res = Edge(data[2], True)
        new_graph.insert_edge(ver1, ver2, new_edge)
        new_graph.insert_edge_res(ver2, ver1, new_edge_res)
    return new_graph


def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]

    test_graph0 = graph_from_tuples(graf_0)
    res0 = ff_ek(test_graph0, test_graph0.get_vertex_inx('s'), test_graph0.get_vertex_inx('t'))
    print(res0)
    print_graph(test_graph0)

    test_graph1 = graph_from_tuples(graf_1)
    res1 = ff_ek(test_graph1, test_graph1.get_vertex_inx('s'), test_graph1.get_vertex_inx('t'))
    print(res1)
    print_graph(test_graph1)

    test_graph2 = graph_from_tuples(graf_2)
    res2 = ff_ek(test_graph2, test_graph2.get_vertex_inx('s'), test_graph2.get_vertex_inx('t'))
    print(res2)
    print_graph(test_graph2)

    test_graph3 = graph_from_tuples(graf_3)
    res3 = ff_ek(test_graph3, test_graph3.get_vertex_inx('s'), test_graph3.get_vertex_inx('t'))
    print(res3)
    print_graph(test_graph3)


main()
