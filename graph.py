import numpy as np

class Graph:
    def __init__(self, filepath):
        V, E = self._process_input(filepath)
        self.V = V
        self.E = E
        
        self.edge_list = self.get_edge_list()
        self.adjacency_list = self.get_adjacency_list()
    
    def _process_input(self, filepath):
        vertices = set()
        edges = set()
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                vertex, adjacent_vertex = line.split(',')[0], line.split(',')[1:]
                vertices.add(vertex)
                for adj in adjacent_vertex:
                    edges.add((vertex, adj))
        return vertices, edges
                
    
    def get_adjacency_matrix(V, E, W):
        pass
    
    def get_edge_list(self):
        return self.E
    
    def get_adjacency_list(self):
        adjacency_list = {}
        for vertex in self.V:
            adjacency_list[vertex] = []
        for edge in self.E:
            u, v = edge
            adjacency_list[u].append(v)
        return adjacency_list
    
    def add_vertices(self, list_vertices):
        for vertex in list_vertices:
            if vertex not in self.V:
                self.V.add(vertex)
                self.adjacency_list[vertex] = []

    def add_edges(self, list_edges):
        for edge in list_edges:
            if edge not in self.E:
                self.E.add(edge)
                self.edge_list.add(edge)
                u, v = edge
                self.add_vertices([u, v])
                self.adjacency_list[u].append(v)
    
    def remove_vertices(self, list_vertices):
        for vertex in list_vertices:
            if vertex in self.V:
                self.V.remove(vertex)
                
                self.E = {edge for edge in self.E if vertex not in edge}
                self.edge_list = self.E
                
                self.adjacency_list.pop(vertex, None)
                for u, adj_list in self.adjacency_list.items():
                    self.adjacency_list[u] = [v for v in adj_list if vertex != v]
                
    def remove_edges(self, list_edges):
        for edge in list_edges:
            if edge in self.E:
                self.E.remove(edge)
                self.edge_list.remove(edge)
                u, v = edge
                if v in self.adjacency_list[u]:
                    self.adjacency_list[u].remove(v)
                    
if __name__ == '__main__':
    graph = Graph('./input.txt')
    print('V', graph.V)
    print('E', graph.E)
    print('adjacency list:', graph.adjacency_list)
    print('remove' + '-' * 30)
    graph.remove_vertices(['1'])
    print('V', graph.V)
    print('E', graph.E)
    print('adjacency list:', graph.adjacency_list)
    
                