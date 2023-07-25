from graph import Graph

# initial Graph constructor
my_graph = Graph()
print("Initial constructor")
my_graph.print_graph()

# adds vertices to graph
my_graph.add_vertex(1)
my_graph.add_vertex(2)
print("\nAdd vertices")
my_graph.print_graph()

# adds an edge to the graph
my_graph.add_edge(1, 2)
print("\nAdd edge")
my_graph.print_graph()