"""
graphDynamicFamilies.py defines classes to create dynamics in graphDynamicsEngines.py

at the moment I don't know if these will have a standard format.

however DynamicFamily(class) must have method __call__ s.t __call__ is a 
dynamic as defined in graphDynamicsEngine.py 

any particular instance of this function will then be instantised there 
"""

import networkx as nx 
import numpy as np 

# Helper Functions  -------------------------------------------------

def comp_array(n): 

    array= np.ones((n,n), dtype = int) - np.identity(n) 
    return array 






# GrindrodBirthDeathFramework and related functions  --------------------------------------------------


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

'''
d=
e=
def temp_death(G):
    return (triadic_closure(G,d,e))

death = temp_death
triad

NOTE: we can just pass a dictionary to this and then unpack using ** 


def funcraper(d,e) 
    return lambda G : triad(G, d, e) 
'''

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




