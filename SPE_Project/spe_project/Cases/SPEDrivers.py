"""
SPEDrivers.py: Defines SPE Drivers for use in GraphSPEModel.py

SPEDriver (function):
    :param G: SPE active graph (including properties)
    :param i: current time step
    :param *args: Remaining args unique to specific driver
    :return: SuperSet of nodes to change (current implementation: List)


from STRUCTURE.md
- SPE driver
    - random samples (taken using bernoulli on the nodes)
    - randomly chosen with fixed size
    - random but weighted using node degree
    - etc
- PLAN
    - make random samples by fixed size work as a first pass
"""

# imports:
import random 
import networkx as nx 
import dynetx as dn

# SPE Drivers ------------------------------------------------------------#

def fixed_size_random(G, i, size = 5 ):
    """
    the subgraph is a copy of the relevant subgraph not a view... it might be better if the edits did automatically carry over
    :param G: active graph
    :param i: timestep. currently unused
    :param size: int
    :return: Subgraph whose nodes are a uniform random sample of given size
    """
    Gnodes = list(G.nodes)
    nodeSample = random.sample(Gnodes ,size)
    return [G.subgraph(nodeSample).copy()]

