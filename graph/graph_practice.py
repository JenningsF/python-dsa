from graph import Graph

# initial Graph constructor
my_graph = Graph()
print("Initial constructor")
my_graph.print_graph()

# adds vertices to Graph
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
print("\nAdd vertices")
my_graph.print_graph()

# adds an edge to the Graph
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')
print("\nAdd edges")
my_graph.print_graph()

# removes an edge from the Graph
my_graph.remove_edge('C', 'B')
print("\nRemove edge")
my_graph.print_graph()

# removes a vertex from the Graph
my_graph.remove_vertex('D')
print("\nRemove vertex")
my_graph.print_graph()