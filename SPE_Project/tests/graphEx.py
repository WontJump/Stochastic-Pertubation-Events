"""
graphEx.py: Testing Code
"""

# imports
import random
import networkx as nx 
import dynetx as dn 
import networkx as nx 
import pandas as pd 
from io import StringIO

stringData = StringIO("""origin_code,destination_code,fare,flow_id
                      1,2,1,10
                      1,3,4,11
                      2,4,3,12
                      2,1,6,13
                      3,4,2,14
                      3,1,1,15
                      4,1,5,16
                      4,2,5,17
                      4,5,3,18
                      5,6,1,19""")

df = pd.read_csv(stringData, sep = ",")
TestGraph = nx.from_pandas_edgelist(df, source = 'origin_code', target = 'destination_code', edge_attr=True, create_using = nx.DiGraph)
flowId = nx.get_edge_attributes(TestGraph,'flow_id')

def graph1(): 
    return TestGraph

stringData = StringIO("""origin_code,destination_code,fare,flow_id
                      1,2,1,10
                      1,3,4,11
                      1,4,3,12
                      1,5,6,13
                      1,6,2,14
                      3,1,1,15
                      4,1,5,16
                      5,4,5,17
                      6,5,3,18
                      2,1,1,19""")

df = pd.read_csv(stringData, sep = ",")
TestGraph2 = nx.from_pandas_edgelist(df, source = 'origin_code', target = 'destination_code', edge_attr=True, create_using = nx.DiGraph)
flowId2 = nx.get_edge_attributes(TestGraph2,'flow_id')

def graph2(): 
    return TestGraph2









# make a dynetx graph. Update it, change parts of it, apply network X functions to it. Specifically: 
# want to take it copy a subgraph chagne that subgraph to a complete graph then send that update to the original 

# arbitarily set n = 15 and use that for a bit of testing 
emptyGraph = nx.empty_graph(15)
edgeList = [(0,1), (2,3), (3,4) , (0,4)]
g = dn.DynGraph(edge_removal = True)
g.add_interactions_from([(0,1), (2,3), (3,4) , (0,4)], t = 0)
print(g)




