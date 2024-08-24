import dynetx as dn 

class GraphSPEModel: 
    def __init__(
    # assumes that init_conditions = {'graph' : NetworkX.Graph, 'attr': dictionary}
        self, 
        graph_dynamics_engine, 
        init_conditions,
        SPE_driver,
        end_time  
        ):

        self.graph_dynamics_engine = graph_dynamics_engine
        self.init_conditions = init_conditions
        self.SPE_driver = SPE_driver 
        self.end_time = end_time 
    

    def graph_initialiser(self): 
        init_graph = self.init_conditions['graph']
        init_attr = self.init_conditions['attr']
        active_graph = dn.DynaGraph(
            data = init_graph, 
            attr = init_attr
        ) 
        return active_graph 


    def change_driver(self, SuperChanges, active_graph): 
        for i in SuperChanges: 
            edge_additions = i['+'] 
            edge_subtractions = i['-']
            edge_attributions = i['attr']
    # this is where the active_graph should be Updated TODO

        pass

    

    def time_step(self, active_graph, SPE_record, i): 

        SuperS = self.SPE_driver(active_graph, i) 
        SPE_record[i] = SuperS 
        SuperChanges = self.graph_dynamics_engine(active_graph, i, SuperS) 
        self.change_driver(SuperChanges, active_graph) 


        

    def timestepper(self): 
        SPE_record = {}
        active_graph = self.graph_initialiser() 
        for i in range(self.end_time): #check the indexing 
            self.time_step(active_graph, SPE_record, i) 

        return active_graph, SPE_record 
    
