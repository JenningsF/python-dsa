class Graph:

    # Graph constructor
    def __init__(self):
        self.adj_list = {}

    # prints out adjacency list of Graph
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

    # removes an edge between two specified vertices
    # if neither vertices exist, then False is returned
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    # removes a specified vertex and all it's edges from the Graph
    # the Graph is bi-directional and allows for efficient vertex removal through for loop
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False