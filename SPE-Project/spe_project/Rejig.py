import dynetx as dn 
import networkx as nx 

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
        self.plusStr = ''
        self.minusStr = ''


    def apply_changes(self, SuperC): 
        for s in SuperC: 
            for e in s.edges: 
                self.active_graph.remove_edge(e) 
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
                self.plusStr.append(i, ' ',j, ' + \n')
            
            for i,j in plus.edges: 
                self.minusStr.append(i, ' ',j, ' - \n')
            




            
        pass


    def difference(self, s, newS):  
        pass


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
            self.time_step(active_graph, SPE_record, i) 

        return active_graph, SPE_record 
    

   