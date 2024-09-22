import networkx as nx 

G = nx.Graph() 
G.add_nodes_from([1,2,3,4,5])

print(G.nodes) 
print(list(G.nodes))