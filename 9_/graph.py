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


class GraphMatrix:

    def __init__(self, value=0):
        self.value = value
        self.graph = []
        self.nodes = {}

    def is_empty(self):
        if not self.nodes:
            return True
        else:
            return False

    def insert_vertex(self, vertex):
        if not self.graph:
            self.graph.append([self.value])
            self.nodes[vertex] = 0
        else:
            for i in range(self.order()):
                self.graph[i].append(self.value)
            new_row = [self.value for i in range(self.order()+1)]
            self.graph.append(new_row)
            self.nodes[vertex] = self.order()

    def insert_edge(self, vertex1, vertex2, edge=1):
        inx1 = self.get_vertex_inx(vertex1)
        inx2 = self.get_vertex_inx(vertex2)
        self.graph[inx1][inx2] = edge
        self.graph[inx2][inx1] = edge

    def delete_vertex(self, vertex):
        inx = self.get_vertex_inx(vertex)
        self.graph.pop(inx)
        for i in range(self.order()-1):
            self.graph[i].pop(inx)
        self.nodes.pop(vertex)
        for i in range(inx, self.order()):
            self.nodes[self.get_vertex(i+1)] = inx
            inx += 1

    def delete_edge(self, vertex1, vertex2):
        inx1 = self.get_vertex_inx(vertex1)
        inx2 = self.get_vertex_inx(vertex2)
        self.graph[inx1][inx2] = self.value
        self.graph[inx2][inx1] = self.value

    def get_vertex_inx(self, vertex):
        return self.nodes[vertex]

    def get_vertex(self, vertex_inx):
        pos = list(self.nodes.values()).index(vertex_inx)
        return list(self.nodes.keys())[pos]

    def neighbours(self, vertex_inx):
        n = []
        for i in range(self.order()):
            if self.graph[vertex_inx][i] != self.value:
                n.append(self.get_vertex(i))
        for i in range(self.order()):
            if self.graph[i][vertex_inx] != self.value and self.get_vertex(i) not in n:
                n.append(self.get_vertex(i))
        return n

    def order(self):
        return len(self.nodes)

    def size(self):
        e = 0
        for i in range(self.order()):
            for j in range(self.order()):
                if self.graph[i][j] != self.value:
                    e += 1
        return e

    def edges(self):
        edg = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.graph[i][j] != self.value:
                    vertex1 = self.get_vertex(i)
                    vertex2 = self.get_vertex(j)
                    edg.append((vertex1, vertex2))
        return edg


class GraphList:

    def __init__(self):
        self.graph = []
        self.nodes = {}

    def is_empty(self):
        if not self.nodes:
            return True
        else:
            return False

    def insert_vertex(self, vertex):
        self.nodes[vertex] = self.order()
        self.graph.append({})

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.nodes.keys() and vertex2 in self.nodes.keys():
            inx1 = self.get_vertex_inx(vertex1)
            inx2 = self.get_vertex_inx(vertex2)
            self.graph[inx1][inx2] = edge
            self.graph[inx2][inx1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.nodes.keys():
            inx = self.get_vertex_inx(vertex)
            for i in range(self.order()):
                for key in self.graph[i].keys():
                    if key == inx:
                        del self.graph[i][key]
                        break
            self.graph.pop(inx)
            self.nodes.pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.nodes.keys() and vertex2 in self.nodes.keys():
            inx1 = self.get_vertex_inx(vertex1)
            inx2 = self.get_vertex_inx(vertex2)
            if inx2 in list(self.graph[inx1].keys()):
                del self.graph[inx1][inx2]
            if inx1 in list(self.graph[inx2].keys()):
                del self.graph[inx2][inx1]

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
    
    def edges_inx(self):
        edg = []
        for i in range(self.order()):
            for k in list(self.graph[i].keys()):
                edg.append((i, k))
        return edg

    def edges_weights(self):
        edg = []
        for i in range(self.order()):
            for k in list(self.graph[i].keys()):
                edg.append((i, k, self.graph[i][k]))
        return edg
