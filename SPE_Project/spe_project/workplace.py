"""
workplace.py
"""

# local imports
import Cases.graphDynamicsEngines as gde
import Cases.initialConditions as ic
import Cases.SPEDrivers as sped
import GraphSPEModel as gspem
import ModelRunner as run 
from Cases.graphDynamicFamilies import rap
# global imports
import networkx as nx 

# Code Begin ---------------------------------------------------------------------

data_path = '/home/wont-jump/Documents/GitHub/Stochastic-Pertubation-Events/SPE_Project/Analytics/Data'
def erdos_rap(n,p): 
    return lambda : nx.erdos_renyi_graph(n,p) 


speGraph = gspem.GraphSPEModel(
    gde.grindrod_triadic,
    lambda G,i: sped.fixed_size_random(G,i,size = 100), 
    end_time = 1500, 
    init_conditions =  erdos_rap(100,0.3),
    random_init = True)

run.bulk_create(speGraph,5,'grindrodTriadicSettings', data_path)


'''
Debug log: 
- the code is running but theres no output.
- both timestep and timestepper are running 
- SuperS is working 
- SuperC is working
- prints arent being called inside record changes 
- looks like record_changes isn't being called 

- Okay weirdly recordChanges and recordTimestep are now being called 
- now it seems that the plus and minus values are wrong. Either theres a 
problem with difference or SuperS or ChangeS
- looks like there is no graph for anything to happen with? The initial graph should have nodes but I'm not convinced it does
- the initial graph works thats not the problem
- when I activate the random sampler in SPEDrivers with an empty graph it returns the right values. It must be being activated 
wrong somehow

- FUCK. The SPE_driver is taking two arguments active_graph and i but i is being taken as the sample size!! bad documentation by me.
- nice we now have a new error to work with 

- OMG it actually works !!!! 
'''