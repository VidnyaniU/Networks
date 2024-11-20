import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges along with their weights (cost)
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=1)

# Find the shortest path from A to D
shortest_path = nx.dijkstra_path(G, source='A', target='D')
path_length = nx.dijkstra_path_length(G, source='A', target='D')

print("Shortest path from A to D:", shortest_path)
print("Length of the shortest path:", path_length)