import numpy as np
from graph import Edge, Vertex
from enum import Enum

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
        for i, li in self.adjacency_list.items():
            for j in li:
                print("( {} , {} )".format(i, j))
                
    def incoming(self, v):
        print("Incoming of {}:".format(v), end=' ')
        for i in range(self.num_vertex):
            if self.adjacent(i, v):
                print("{}".format(i), end=' ')
        print()

    def outgoing(self, v):
        print("Outgoing of {}:".format(v), end=' ')
        for i in self.adjacency_list[v]:
            print("{}".format(i), end=' ')
        print()

    def add_vertex(self, u):
        if u not in self.adjacency_list.keys():
            self.adjacency_list[u] = []
            self.num_vertex += 1
            
    def del_vertex(self, u):
        for vertex, li in self.adjacency_list.items():
            self.adjacency_list[vertex] = [v for v in li if v != u]
        if u in self.adjacency_list:
            self.adjacency_list.pop(u, None)
            self.num_vertex -= 1
             
    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        if self.adjacent(source, target) is False:
            self.adjacency_list[source].append(target)

    def del_edge(self, source, target):
        if self.adjacent(source, target):
            self.adjacency_list[source].remove(target)

class VertexMapping:
    def __init__(self):
        self._incoming_edges = object()
        self._outcoming_edges = object()

class ExtendedAdjacencyList:
    def __init__(self, input_file):
        with open(input_file, 'r') as wf:
            lines = wf.readlines()

        self.num_vertex = int(lines[0].strip())
        self.adjacency_list = {}
        for i in range(self.num_vertex):
            self.adjacency_list[i] = VertexMapping()
            self.adjacency_list[i]._incoming_edges = []
            self.adjacency_list[i]._outcoming_edges = []
            
        print(len(self.adjacency_list[0]._outcoming_edges))
        for line in lines[1:]:
            data = line.strip().split(',')
            # blank line
            if data[0] == '':
                continue
            line = list(map(int, data))
            source = line[0]
            targets = line[1:]
            for tg in targets:
                edge = Edge(source, tg, f'{source}->{tg}')
                self.adjacency_list[source]._outcoming_edges.append(edge)
                self.adjacency_list[tg]._incoming_edges.append(edge)
                
    def adjacent(self, u, v):
        for edge in self.adjacency_list[u]._outcoming_edges:
            if v == edge.target():
                return True
        return False
    
    def _print(self):
        print("Extended Adjacency List:")
        for i in range(self.num_vertex):
            print(f'Incoming to Vertex {i}:', end='')
            for edge in self.adjacency_list[i]._incoming_edges:
                print(edge)
            print()
            print(f'Outcoming to Vertex {i}:', end='')
            for edge in self.adjacency_list[i]._outcoming_edges:
                print(edge)
            print()
            
    def print_edge_list(self):
        print("Edge List:")
        for i in self.adjacency_list:
            for edge in self.adjacency_list[i]._outcoming_edges:
                print("( {} , {} )".format(edge.source(), edge.target()))
                
    def incoming(self, v):
        print("Incoming of {}:".format(v), end=' ')
        for edge in self.adjacency_list[v]._incoming_edges:
            print(edge.source(), end=' ')

    def outgoing(self, v):
        print("Outgoing of {}:".format(v), end=' ')
        for edge in self.adjacency_list[v]._outcoming_edges:
            print(edge.target(), end=' ')

    def add_vertex(self, u):
        if u not in self.adjacency_list.keys():
            self.adjacency_list[u] = VertexMapping()
            self.adjacency_list[u]._incoming_edges = []
            self.adjacency_list[u]._outcoming_edges = []
            self.num_vertex += 1
            
    def del_vertex(self, u):
        for vertex in self.adjacency_list:
            self.del_edge(vertex, u)
            self.del_edge(u, vertex)
        if u in self.adjacency_list:
            self.adjacency_list.pop(u, None)
            self.num_vertex -= 1
    
    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        if self.adjacent(source, target) is False:
            edge = Edge(source, target, f'{source}->{target}')
            self.adjacency_list[source]._outcoming_edges.append(edge)
            self.adjacency_list[target]._incoming_edges.append(edge)
    
    def del_edge(self, source, target):
        if self.adjacent(source, target):
            self.adjacency_list[source]._outcoming_edges = [
                edge for edge in self.adjacency_list[source]._outcoming_edges if edge.target() != target
            ]
            self.adjacency_list[target]._incoming_edges = [
                edge for edge in self.adjacency_list[target]._incoming_edges if edge.source() != source
            ]
            
            
class AdjacencyMap:
    def __init__(self, input_file):
        with open(input_file, 'r') as wf:
            lines = wf.readlines()

        self.num_vertex = int(lines[0].strip())
        self.adjacency_list = {}
        for i in range(self.num_vertex):
            self.adjacency_list[i] = VertexMapping()
            self.adjacency_list[i]._incoming_edges = {}
            self.adjacency_list[i]._outcoming_edges = {}

        for line in lines[1:]:
            data = line.strip().split(',')
            # blank line
            if data[0] == '':
                continue
            line = list(map(int, data))
            source = line[0]
            targets = line[1:]
            for tg in targets:
                edge = Edge(source, tg, f'{source}->{tg}')
                self.adjacency_list[source]._outcoming_edges[tg] = edge
                self.adjacency_list[tg]._incoming_edges[source] = edge
                
    def adjacent(self, u, v):
        return v in self.adjacency_list[u]._outcoming_edges
    
    def _print(self):
        print("Adjacency Map:")
        for i in range(self.num_vertex):
            print(f'Incoming to Vertex {i}:', end='')
            for edge in self.adjacency_list[i]._incoming_edges:
                print(edge)
            print()
            print(f'Outcoming to Vertex {i}:', end='')
            for edge in self.adjacency_list[i]._outcoming_edges:
                print(edge)
            print()
            
    def print_edge_list(self):
        print("Edge List:")
        for i in range(self.num_vertex):
            for edge in self.adjacency_list[i]._outcoming_edges.values():
                print("( {} , {} )".format(edge.source(), edge.target()))
                
    def incoming(self, v):
        print("Incoming of {}:".format(v), end=' ')
        for edge in self.adjacency_list[v]._incoming_edges:
            print(edge.source(), end=' ')

    def outgoing(self, v):
        print("Outgoing of {}:".format(v), end=' ')
        for edge in self.adjacency_list[v]._outcoming_edges:
            print(edge.target(), end=' ')

    def add_vertex(self, u):
        if u not in self.adjacency_list.keys():
            self.adjacency_list[u] = VertexMapping()
            self.adjacency_list[u]._incoming_edges = {}
            self.adjacency_list[u]._outcoming_edges = {}
            self.num_vertex += 1
            
    def del_vertex(self, u):
        for vertex in self.adjacency_list:
            self.del_edge(vertex, u)
            self.del_edge(u, vertex)
        if u in self.adjacency_list:
            self.adjacency_list.pop(u, None)
            self.num_vertex -= 1
    
    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        if self.adjacent(source, target) is False:
            edge = Edge(source, target, f'{source}->{target}')
            self.adjacency_list[source]._outcoming_edges[target] = edge
            self.adjacency_list[target]._incoming_edges[source] = edge
    
    def del_edge(self, source, target):
        if self.adjacent(source, target):
            self.adjacency_list[source]._outcoming_edges = {
                v: edge
                for v, edge in self.adjacency_list[source]._outcoming_edges.items()
                    if edge.target() != target
            }
            self.adjacency_list[target]._incoming_edges = {
                v: edge 
                for v, edge in self.adjacency_list[target]._incoming_edges.items() 
                    if edge.source() != source
            }

    def subgraph_by_high(self, root, high=1):
        if high == 0:
            return
        v = self._data[root]
        for w in v._outgoing:
            e = v._outgoing[w]
            print("( {} , {} )".format(e.source(), e.target()))
            self.subgraph_by_high(e.target(), high - 1)