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

# Dynamics: -------------------------------------------------------

def graph_completer(G, active_graph, i): 
    return nx.complete_graph(G.nodes)
