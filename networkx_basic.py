import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()
G = nx.DiGraph()

# G = nx.MultiGraph()
# G = nx.MultiDiGraph()

G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')

G.add_edge('A', 'B')
G.add_edge('B', 'A')
G.add_edge('A', 'C')
G.add_edge('C', 'A')
G.add_edge('C', 'E')
G.add_edge('B', 'D')
G.add_edge('B', 'F')
G.add_edge('F', 'E')

nx.draw(G, with_labels=True)
plt.show()