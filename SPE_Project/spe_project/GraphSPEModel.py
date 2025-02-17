'''

GraphSPEModel.py: Creates and simulates an SPE graph, given a dynamic and SPE driver

SPE = Stochastic Permutation Events

timestep is everything that happens in a time step namely:
    - SPE_driver chooses the sets where the dynamics will take place
    - SuperC is the set of all 'new graphs' after the dynamic takes place 
    - apply_changes applys these changes to the current graph 
    - record_timestep records all the stuff that happens 

'''

#imports
import networkx as nx

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
        random_init = False 
        ):
        """
        :param dynamic: Dynamic defined in graphDynamicsEngines.py
        :param SPE_driver: SPEDriver defined in SPEDrivers.py
        :param end_time: integer for time step to stop at (aka number of timesteps ran)
        :param init_conditions: nx.Graph object the SPE graph starts as
        :param random_init: sometime its useful to have the model randomly generate the init_conditions every time the 
        model is run (for example in the model runner)

        if random_init = true then init_conditions has to be a function which returns another function which takes no params
        and returns a graph on calling 

        

        """
        self.dynamic = dynamic
        self.SPE_driver = SPE_driver 
        self.end_time = end_time

        self.init_conditions = init_conditions
        self.random_init = random_init 

        if random_init: 
            self.active_graph = init_conditions()
        else:
            self.active_graph = init_conditions

        self.SPE_dict = {}
        self.Change_dict = {}
        self.history = ''
        self.initial_record = '' + str(self.active_graph.number_of_nodes) + '\n'

        for k,j in self.active_graph.edges: 
            k,j = str(k), str(j)
            # should use joins for this 
            plusStr = ' '.join([ k , j ,'+', '0' + '\n' ])
            self.initial_record += plusStr

           

             


    def apply_changes(self, SuperC): 
        for s in SuperC: 
            for e in s.edges: 
                i,j = e
                self.active_graph.remove_edge(i,j) 
            self.active_graph.update(SuperC[s])


    def record_timestep(self, SuperS, SuperC, i): 
        self.SPE_dict[i] = [{'Nodes': S.nodes, 'Edges' : S.edges} for S in SuperS]
        self.record_changes(SuperC,i)
        
        pass
    
    def record_changes(self, SuperC,i):
        i = str(i + 1) # I've added one here so I can record the initial graph as edges added at time 0 
        for s in SuperC: 
            # at the moment this wont do attributes and difference will never handle attributes 
            plus = nx.difference(SuperC[s], s)
            minus = nx.difference(s, SuperC[s]) 


            for k,j in plus.edges: 
                k,j = str(k), str(j)
                # should use joins for this 
                plusStr = ' '.join([ k , j ,'+', i + '\n' ])
                self.history += plusStr

            for k,j in minus.edges: 
                k,j = str(k), str(j)
                minusStr = ' '.join([ k , j ,'-', i + '\n' ])
                self.history += minusStr

    def super_changes(self, SuperS, i): 
        SuperC = {}
        for s in SuperS: 
            newS = self.dynamic(s, self.active_graph, i)
            SuperC[s] = newS
        return SuperC 

    def time_step(self, i):
        """
        Simulates 1 time step.
        :param i: time step index
        """
        SuperS = self.SPE_driver(self.active_graph, i) 
        SuperC = self.super_changes(SuperS, i) 
        self.apply_changes(SuperC)
        self.record_timestep(SuperS,SuperC, i)


    def timestepper(self):
        """
        timestepper calls time_step from for each time step from 0 to end_time-1
        """
        if self.random_init: 
            self.active_graph = self.init_conditions()
        else: 
            self.active_graph = self.init_conditions

        self.SPE_dict = {}
        self.Change_dict = {}
        self.history = ''

        active_graph = self.active_graph  # I don't think i ever use this variable? 
        
        for i in range(self.end_time): #check the indexing 
            self.time_step(i) 
    
    def file_record(self, file_name): 
        """
        returns a file in dynetx format with the SPE_dict 
        dynetx: https://dynetx.readthedocs.io/en/latest/tutorial.html#creating-a-graph 
        :param file_name: name of file created 
        """
        with open(file_name, 'w') as file: 
            file.write('file format 001')
            file.write(str(self.SPE_dict) + '\n')
            file.write(self.initial_record)
            file.write(self.history)


    '''
    the file format string is meant to give a way of knowing what old formats for data recordings were
    
    001:
    file format string 
    SPE dict record in timestep : nodes: , edges: format 
    initial record first number of nodes in the initial graph and then additions in dynetx form 
    the dynetx form history 

    
    '''