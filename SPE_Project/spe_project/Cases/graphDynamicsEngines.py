"""
graphDynamicsEngines.py: Defines dynamics to be used in GraphSPEModel.py

Dynamic (function):
    :param G: superset of nodes to change
    :param active_graph: SPE graph (nx.Graph object)
    :param i: current time step


from STRUCTURE.md, Potential dynamics to add:
    - graph dynamics engine
        - random rewiring
        - toggling all edges on to off
        - add 1 or minus 1 to all edge weights


    NOTE that all dynamics must have the active_graph and i variable
    maybe this could be added in a custom decorator?

"""

# imports:
# import itertools as it
import networkx as nx 
import numpy as np 
from Cases.graphDynamicFamilies import * # polutes namespace? 

# Dynamics: -------------------------------------------------------

def graph_completer(G, active_graph, i): 
    """
    returns a complete graph on the same set of nodes as G 

    :param G: networkX graph object 
    """
    return nx.complete_graph(G.nodes)

traidic_closure_with_random_death = GrindrodBirthDeathFrameWork(
    death = rap(random_birth_or_death_noise,{'p': 0.99 }) ,
    birth = rap(triadic_closure, {'d' : 0.2, 'e': 0.04}) 
    ) # this should work for samples less than 20 (note this is the size of S in SuperS not the total graph) 