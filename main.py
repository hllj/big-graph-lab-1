from representation import AdjacencyMatrix, AdjacencyList, ExtendedAdjacencyList, AdjacencyMap
from graph import Vertex


def main():
    input_file = r"./input.txt"
    adjacency_matrix = AdjacencyMap(input_file)
    # adjacency_matrix.print_adjacency_matrix()
    adjacency_matrix.print_edge_list()
    # adjacency_matrix.incoming(2)
    # adjacency_matrix.outgoing(0)
    adjacency_matrix.del_edge(source=0, target=1)
    adjacency_matrix.print_edge_list()

    # graph = Graph(input_file)
    # graph.print_edge_list()
    # graph.subgraph_by_high(Vertex(5), high=2)

    # input_file = r"./input_words.txt"
    # graph = Graph(input_file)
    # graph.print_vertices()


if __name__ == "__main__":
    main()
