import numpy as np 
import networkx as nx 

mat = np.array([[0,1], [ 1, 0]])
graph = nx.stochastic_block_model([1,1], mat) 

print(graph) 