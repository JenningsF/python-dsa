class Graph:

    # Graph constructor
    def __init__(self):
        self.adj_list = {}

    # prints out adjacency list of graph
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
        if not self.adj_list:
            print(self.adj_list)

    # adds specified vertex to the adjacency list of Graph
    # if vertex already exists, then False is returned
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # adds an edge between two specified vertices 
    # if neither vertices exist, then False is returned
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
