
import random 
import networkx as nx 
import dynetx as dn 

''' from STRUCTURE.md 
- SPE driver 
    - random samples (taken using bernoulli on the nodes)
    - randomly chosen with fixed size 
    - random but weighted using node degree 
    - etc 
- PLAN 
    - make random samples by fixed size work as a first pass
'''
#------------------------------------------------------------#

'''
the only rules for the SPEdriver are 

SuperS = self.SPE_driver(active_graph, i) 

it takes the active_graph (including properties) and the time step and returns a set of sets (might not be sets in implementation) 

'''

def fixed_size_random(G, size = 2): 
    '''
    takes active graph and a size parameter
    returns a subgraph whos nodes are a uniform random sample of size 'size' 
    the subgraph is a copy of the relevant subgraph not a view... it might be better if the edits did automatically carry over
    '''
    Gnodes = list(G.nodes)
    nodeSample = random.sample(Gnodes ,size)
    return [G.subgraph(nodeSample).copy()]

