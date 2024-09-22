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

def rap(func, kwargs): 
    return lambda G: func(G, **kwargs)




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

    def dynamic(self, G, active_graph, i): # be careful! when does this G become an array and when is it a Graph this is unclear
        arr = nx.adjacency_matrix(G)   
        n = arr.shape[0]
        I = comp_array(n)

        dyn = (I - self.death(arr)) * arr + self.birth(arr) * (I - arr)  
        graph_instance = nx.stochastic_block_model([1 for i in range(n)], dyn, nodelist = list(G.nodes))

        return graph_instance


    def __call__(self, G, active_graph, i):
        return self.dynamic(G, active_graph, i) 


# I might have to wrap this in some sort of function in order to call it within the class (this is because it requires d,e to
# be called but the class wont know to include those parameters)
def traidic_closure(G, d, e):
    """
    :param d real \in [0,1]
    :param e real \in [0, (1 - d)/(n - 2)] 

    """ 
    n = G.shape[0]  

    if not 0 < e < (1-d)/(n-2):
        raise ValueError(' e must be in the interval 0 < e < (1-d)/(n-2)')
    if n<2: 
        raise ValueError(' n must be >= 2')
    
    I = comp_array(n) 
    return (d*I) + (e*I)*(G @ G) 

def random_birth_or_death_noise(G,p): 
    I = comp_array(G.shape[0]) 
    return p*I

# ah okay so stochastic block model must be making a new node set which then fucks something else over 