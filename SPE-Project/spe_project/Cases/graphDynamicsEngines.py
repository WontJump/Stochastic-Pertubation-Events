"""
graphDynamicsEngines.py: Defines dynamics to be used in GraphSPEModel.py

Dynamic (function):
    :param G: superset of nodes to change
    :param active_graph: SPE graph (nx.Graph object)
    :param i: current time step


DynamicFamily(class): 
    :param func1 ... funcN Dynamics as defined above
allow class instances to be called as functions for use within GraphSPEModel.py
NOTE this call function must itself be a dynamic 




from STRUCTURE.md:
    - graph dynamics engine
        - random rewiring
        - complete graph insertion
        - toggling all edges on to off
        - add 1 or minus 1 to all edge weights
    - init conditions ( I think these are all included in netex)
-plan:
    - make complete graph insertion first
    - followed by random rewiring

    NOTE that all dynamics must have the active_graph and i variable
    maybe this could be added in a custom decorator?

useful functions 
nx.adjacency_matrix(G) returns an adjacency NUmpy array 
* or np.multiply for termwise multiplication of termwise multiplication 
@ does matrix mult now! (but this doesnt really matter)
need the complete matrix denoted 1? (probably just use the 1's matrix minus the identity) 


"""

# imports:
# import itertools as it
import networkx as nx 
import numpy as np 
# helper functions ( to be moved to another file) -------------------------------------------------

def comp_array(n): 

    array= np.ones((n,n), dtype = int) - np.identity(n) 
    return array 

# Dynamics: -------------------------------------------------------

def graph_completer(G, active_graph, i): 
    return nx.complete_graph(G.nodes)



   

#classes to construct Dynamic families: -------------------------------------------------------
 

class GrindrodBirthDeathFrameWork:
    def __init__(self, death, birth):
        self.death = death
        self.birth= birth 
        """
        param death_func defined in graphDynamicsEngines.py 
        param birth_func defined in graphDynamicsEngines.py  

        """
        pass

    def dynamic(self, G, active_graph, i): 
        n = len(G) 
        I = comp_array(n)
        G = nx.adjacency_matrix(G)

        dyn = (I - self.death(G)) * G + self.birth(G) * (I - G)  
        graph_instance = nx.stochastic_block_model(np.ones(n), dyn)

        return graph_instance


    def __call__(self, G, active_graph, i):
        return self.dynamic(G, active_graph, i) 
 

# array based mechanisms -----------------------------------------------------------------
"""
array_mechanism(function) 
    : param G adjacency matrix of an undirected graph np.array 

currently its not passed the whole graph or the time but there isn't any reason for this. 

"""

# I might have to wrap this in some sort of function in order to call it within the class (this is because it requires d,e to
# be called but the class wont know to include those parameters)
def traidic_closure(G, d, e):
    """
    :param d real \in [0,1]
    :param e real \in [0, (1 - d)/(n - 2)] 

    """ 
    n = G.ndim 

    if not 0 < e < (1-d)/(n-2):
        raise ValueError(' e must be in the interval 0 < e < (1-d)/(n-2)')
    if n<2: 
        raise ValueError(' n must be >= 2')
    
    I = comp_array(n) 
    return (d*I) + (e*I)*(G @ G) 

def random_birth_or_death_noise(G,p): 
    I = comp_array(G.ndim) 
    return p*I 

    
