from graph import Graph

# initial Graph constructor
my_graph = Graph()
print("Initial constructor")
my_graph.print_graph()

# adds vertices to graph
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
print("\nAdd vertices")
my_graph.print_graph()

# adds an edge to the graph
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')
print("\nAdd edges")
my_graph.print_graph()

# removes an edge from the graph
my_graph.remove_edge('A', 'B')
my_graph.remove_edge('A', 'D')
print("\nRemove edge")
my_graph.print_graph()