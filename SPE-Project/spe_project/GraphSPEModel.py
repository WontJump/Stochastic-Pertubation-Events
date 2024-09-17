import dynetx as dn 
import networkx as nx 
'''
timestepper controls how many timesteps are triggered 
timestep is everything that happens in a time step namely: 
    - SPE_driver chooses the sets where the dynamics will take place
    - SuperC is the set of all 'new graphs' after the dynamic takes place 
    - apply_changes applys these changes to the current graph 
    - record_timestep records all the stuff that happens 

'''

def SuperSChecker(SuperS): 
    for s in SuperS: 
        print('this is the graph to be checked:',  s)
        print('edges are:')
        for e in s.edges:
            print(e) 
        print('nodes are:')
        for n in s.nodes: 
            print(n) 
        

class GraphSPEModel: 
    def __init__(
        self, 
        dynamic, 
        SPE_driver,
        end_time = 5, 
        init_conditions = nx.Graph() ,
        ):

        self.dynamic = dynamic
        self.SPE_driver = SPE_driver 
        self.end_time = end_time
        self.active_graph = init_conditions

        self.SPE_dict = {}
        self.Change_dict = {}
        self.history = ''


    def apply_changes(self, SuperC): 
        for s in SuperC: 
            for e in s.edges: 
                i,j = e
                self.active_graph.remove_edge(i,j) 
            self.active_graph.update(SuperC[s])


    def record_timestep(self, SuperS, SuperC, i): 
        self.SPE_dict[i] = SuperS 
        self.record_changes(SuperC,i)
        
        pass
    
    def record_changes(self, SuperC,i):
        for s in SuperC: 
            # at the moment this wont do attributes and difference will never handle attributes 
            plus = nx.difference(SuperC[s], s)
            minus = nx.difference(s, SuperC[s]) 


            for i,j in plus.edges: 
                # self.history.append(i, ' ',j, ' + \n')
                print(i, ' ',j, ' + \n') 
            for i,j in minus.edges: 
                # self.history.append(i, ' ',j, ' - \n')
                print(i, ' ',j, ' - \n') 


    def super_changes(self, SuperS, i): 
        SuperC = {}
        for s in SuperS: 
            newS = self.dynamic(s, self.active_graph, i)
            SuperC[s] = newS
        return SuperC 

    def time_step(self, i):
        SuperS = self.SPE_driver(self.active_graph, i) 
        SuperC = self.super_changes(SuperS, i) 
        self.apply_changes(SuperC)
        self.record_timestep(SuperS,SuperC, i)


    def timestepper(self): 
        SPE_record = {}
        active_graph = self.active_graph
        for i in range(self.end_time): #check the indexing 
            self.time_step(i) 
        print(self.history)
    
