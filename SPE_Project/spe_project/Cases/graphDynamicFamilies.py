"""
graphDynamicFamilies.py defines classes to create dynamics in graphDynamicsEngines.py

at the moment I don't know if these will have a standard format.

however DynamicFamily(class) must have method __call__ s.t __call__ is a 
dynamic as defined in graphDynamicsEngine.py 

any particular instance of this function will then be instantised there 
"""

import networkx as nx 
import numpy as np 
import copy as copy 

# Helper Functions  -------------------------------------------------

def comp_array(n):
    """
    returns the array of all 1's except for the diagonal which is 0. The adjacency matrix of a complete
    undirect graph on n nodes

    :param n: size of the square array 
    """ 

    array= np.ones((n,n), dtype = int) - np.identity(n) 
    return array 

def rap(func, kwargs): 
    """
    simple rapper to allow the GrindrodBirthDeathFrameWork to call functions like triadic closure 

    :param func: function to be rapped 
    :param kwags: kwargs (not including G) to be passed as a dictionary 
    """
    return lambda G, active_graph, i: func(G, active_graph, i, **kwargs) # Now I'm changing birth death to automatically take G, activeG and i 
# I don't know if this will still work 





# GrindrodBirthDeathFramework and related functions  --------------------------------------------------


class GrindrodBirthDeathFrameWork:
    def __init__(self, death, birth):
        self.death = death
        self.birth= birth 
        """
        General family of Dynamics defined this paper https://www.maths.ed.ac.uk/~dhigham/Publications/P111.pdf

        :param death_func: function defined below must take and return arr rather than graphs 
        :param birth_func: similarly to above  

        """
        pass

    def dynamic(self, G, active_graph, i): # be careful! when does this G become an array and when is it a Graph this is unclear
        arr = nx.adjacency_matrix(G)   
        n = arr.shape[0]
        I = comp_array(n)

        dyn = (I - self.death(G, active_graph, i)) * arr + self.birth(G, active_graph, i) * (I - arr)  
        graph_instance = nx.stochastic_block_model([1 for i in range(n)], dyn, nodelist = list(G.nodes))

        return graph_instance


    def __call__(self, G, active_graph, i):
        return self.dynamic(G, active_graph, i) 


# I might have to wrap this in some sort of function in order to call it within the class (this is because it requires d,e to
# be called but the class wont know to include those parameters)
def triadic_closure(G, active_graph, i, d, e):
    """
    triadic closure model defined in https://www.maths.ed.ac.uk/~dhigham/Publications/P111.pdf  

    :param d real \in [0,1]
    :param e real \in [0, (1 - d)/(n - 2)] 

    """ 

    arr = nx.adjacency_matrix(G)   
    n = arr.shape[0]  

    if not 0 < e < (1-d)/(n-2):
        raise ValueError(' e must be in the interval 0 < e < (1-d)/(n-2)')
    if n<2: 
        raise ValueError(' n must be >= 2')
    
    I = comp_array(n) 
    return (d*I) + (e*I)*(arr @ arr) 

def random_birth_or_death_noise(G,active_graph, i,p): 
    """
    random noise to be used in the grindrod framework 

    :param G: graph! no longer takes arrays  
    :param p: probability of edge birth/death 
    
    """
    arr = nx.adjacency_matrix(G)
    I = comp_array(arr.shape[0]) 
    return p*I

# ah okay so stochastic block model must be making a new node set which then fucks something else over 


def inner_triadic_closure(G, active_graph, i , d, out_lim, in_lim):
    """
    :param d: as in traidic closure chance of random edge birth 
    :param out_lim: upper bound on the amount of probability open traingles from outside S \in SuperS can add to edge formation
    :param in_lim: limit on the amount of probability from triangles inside S 
    """
    size_g = len(G)
    size_active = len(active_graph)


    H = copy.deepcopy(G) # this whole thing is riddle with performance issues 
    extraNodes = [i for i in active_graph.nodes if i not in H.nodes]
    H.add_nodes_from(extraNodes)

    graph_in = nx.adjacency_matrix(G)
    graph_out = nx.adjacency_matrix(nx.difference(active_graph,H))

    e_1 = out_lim/(size_active - size_g)
    e_2 = in_lim/(size_g - 2) 

    graph_out_squared = graph_out @ graph_out
    graph_out_squared = graph_out_squared[np.ix_(G.nodes, G.nodes)]

    # print(Gnodes)
    # print(graph_out_squared)
    # print(graph_in.shape)
    # print(graph_out_squared.shape)
    # exit()

    I = comp_array(size_g)

    return d*I + (e_1*(graph_out_squared) + e_2 *(graph_in @ graph_in)) 
   