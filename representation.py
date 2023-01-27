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

    def adjacent(self, u, v):
        return self.graph[u][v]

    def _print(self):
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

class AdjacencyList:
    def __init__(self, input_file):
        with open(input_file, 'r') as wf:
            lines = wf.readlines()

        self.num_vertex = int(lines[0].strip())
        self.adjacency_list = {}
        for i in range(self.num_vertex):
            self.adjacency_list[i] = []

        for line in lines[1:]:
            data = line.strip().split(',')
            # blank line
            if data[0] == '':
                continue
            line = list(map(int, data))
            source = line[0]
            targets = line[1:]
            for tg in targets:
                self.adjacency_list[source].append(tg)
    
    def adjacent(self, u, v):
        return v in self.adjacency_list[u]
    
    def _print(self):
        print("Adjacency List:")
        for i in range(self.num_vertex):
            print(self.adjacency_list[i])
            
    def print_edge_list(self):
        print("Edge List:")
        for i in range(self.num_vertex):
            for j in self.adjacency_list[i]:
                print("( {} , {} )".format(i, j))
                
    def incoming(self, v):
        print("Incoming of {}:".format(v), end=' ')
        for i in range(self.num_vertex):
            if self.adjacent(i, v):
                print("{} ".format(i), end='')

    def outgoing(self, v):
        print("Outgoing of {}:".format(v), end=' ')
        for i in self.adjacency_list[v]:
            print("{} ".format(i), end='')

    def del_edge(self, source, target):
        if self.adjacent(source, target):
            self.adjacency_list[source].remove(target)
            
