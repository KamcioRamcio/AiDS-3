import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# simple undirected graph
# -- 
G = nx.Graph()
#edge from node 1 to node 2
# by creacting and edge you are creating a node simple as that 
G.add_edge(1, 2)
# you can add weight to the edge, define it as you want, maybe its gonna be the speed of the connection and when is higher is better or 
# you can use it as a distance between two nodes and when is lower is better, go play with it (śmiesznie sie tak po angliesku pisze poradnik XD, zeby brzmiał poważnie)
G.add_edge(2, 3, weight=0.9)

# how you can use add_egde 
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_node("D")


nx.draw_spring(G, with_labels=True) 
plt.show()
# directed graph
# --
DG = nx.DiGraph()

# multi undirected graph, mean that from one node to another node can have multiple edges
# --
MG = nx.MultiGraph()

# multi directed graph
# --
MDG = nx.MultiDiGraph()


