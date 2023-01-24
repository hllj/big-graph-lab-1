import numpy as np


class AdjacencyMatrix:
    def __init__(self, input_file):
        with open(input_file, 'r') as wf:
            lines = wf.readlines()

        self.num_vertex = int(lines[0].strip())
        self.graph = np.zeros((self.num_vertex, self.num_vertex), dtype=np.uint32)

        for line in lines[1:]:
            data = line.strip().split(',')
            # blank line
            if data[0] == '':
                continue
            line = list(map(int, data))
            source = line[0]
            targets = line[1:]
            for tg in targets:
                self.graph[source][tg] = 1

    def print_adjacency_matrix(self):
        print("Adjacency Matrix:")
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                print(self.graph[i][j], end=' ')
            print()

    def print_edge_list(self):
        print("Edge List:")
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                if self.graph[i][j] == 1:
                    print("( {} , {} )".format(i, j))

    def incoming(self, v):
        print("Incoming of {}:".format(v), end=' ')
        for i in range(self.num_vertex):
            if self.graph[i][v] == 1:
                print("{} ".format(i), end='')

    def outgoing(self, v):
        print("Outgoing of {}:".format(v), end=' ')
        for i in range(self.num_vertex):
            if self.graph[v][i] == 1:
                print("{} ".format(i), end='')

    def del_edge(self, source, target):
        self.graph[source][target] = 0


class Vertex:
    def __init__(self, label):
        self._label = label

    def label(self):
        return self._label

    def __str__(self):
        return str(self._label)


class Edge:
    def __init__(self, source, target, label):
        self._source = source
        self._target = target
        self._label = label

    def source(self):
        return self._source

    def target(self):
        return self._target

    def label(self):
        return self._label

    def opposite(self, v):
        if v is self._source:
            return self._target
        else:
            return self._source

    def __str__(self):
        return str(self._label)


class Graph:
    def __init__(self, input_file):
        self._data = dict()
        self.create_graph(input_file)

    def new_vertex(self, label):
        v = Vertex(label)
        self._data[v] = type(str(), (), {})
        self._data[v]._incoming = dict()
        self._data[v]._outgoing = dict()
        return v

    def new_edge(self, source, target, label=None):
        e = Edge(source, target, label)
        self._data[source]._outgoing[target] = e
        self._data[target]._incoming[source] = e

    def create_graph(self, input_file):
        with open(input_file, 'r') as wf:
            lines = wf.readlines()

        vertices = dict()
        for line in lines[1:]:
            data = line.strip().split(',')
            # blank line
            if data[0] == '':
                continue
            # line = list(map(int, data))
            source = data[0]
            targets = data[1:]

            if source not in vertices:
                vertices[source] = self.new_vertex(source)
            for tg in targets:
                if tg not in vertices:
                    vertices[tg] = self.new_vertex(tg)
                self.new_edge(vertices[source], vertices[tg])

    def print_edge_list(self):
        for v in self._data:
            for w in self._data[v]._outgoing:
                e = self._data[v]._outgoing[w]
                print("( {} , {} )".format(e.source(), e.target()))

    def print_vertices(self):
        all_vertices = [str(vt) for vt in self._data.keys()]
        all_vertices.sort()
        for vertex in all_vertices:
            print(vertex)


def main():
    # input_file = r"./input.txt"
    # adjacency_matrix = AdjacencyMatrix(input_file)
    # # adjacency_matrix.print_adjacency_matrix()
    # adjacency_matrix.print_edge_list()
    # # adjacency_matrix.incoming(2)
    # # adjacency_matrix.outgoing(0)
    # adjacency_matrix.del_edge(source=0, target=1)
    # adjacency_matrix.print_edge_list()

    # graph = Graph(input_file)
    # graph.print_edge_list()

    input_file = r"./input_words.txt"
    graph = Graph(input_file)
    graph.print_vertices()


if __name__ == "__main__":
    main()
