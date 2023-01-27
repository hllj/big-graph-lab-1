from representation import AdjacencyMatrix, AdjacencyList, ExtendedAdjacencyList, AdjacencyMap

def main():
    input_file = r"./input.txt"
    adjacency_matrix = ExtendedAdjacencyList(input_file)
    # adjacency_matrix.print_adjacency_matrix()
    adjacency_matrix.print_edge_list()
    # adjacency_matrix.incoming(2)
    # adjacency_matrix.outgoing(0)
    adjacency_matrix.del_edge(source=0, target=1)
    adjacency_matrix.print_edge_list()

    # graph = Graph(input_file)
    # graph.print_edge_list()

    # input_file = r"./input_words.txt"
    # graph = Graph(input_file)
    # graph.print_vertices()


if __name__ == "__main__":
    main()