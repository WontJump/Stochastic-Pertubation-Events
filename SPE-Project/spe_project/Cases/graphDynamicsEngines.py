import itertools as it 
import networkx as nx 
 
'''from STRUCTURE.md: 
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
'''

def graph_completer(G, active_graph, i): 
    return nx.complete_graph(G.nodes)