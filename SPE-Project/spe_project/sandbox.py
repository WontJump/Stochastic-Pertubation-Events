import dynetx as dn 
import networkx as nx

g = dn.DynGraph(edge_removal=True)
g.add_interaction(u=4, v=2, t=0)
g.add_interactions_from([(1, 2), (2, 3), (3, 1)], t=2)
print(g)

g.remove_edge(u = 4, v= 2)

dn.write_interactions(g, 'graphFile.txt')
print(g)