import Cases.graphDynamicsEngines as gde
import Cases.initialConditions as ic 
import Cases.SPEDrivers as sped

import GraphSPEModel as gspem
import networkx as nx 

speGraph = gspem.GraphSPEModel(gde.graph_completer, sped.fixed_size_random, end_time = 2, init_conditions =  nx.empty_graph(5))
speGraph.timestepper()
