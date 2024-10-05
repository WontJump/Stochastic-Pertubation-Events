import networkx as nx 

def erdos_rap(n,p): 
    return nx.erdos_renyi_graph(n,p)

if erdos_rap(100, 0.3) == erdos_rap(100, 0.3): 
    print('fuck') 
else: 
    print('ok')