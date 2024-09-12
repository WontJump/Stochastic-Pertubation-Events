
# Pipe line 

- Graph initialised  [graph_initialiser(self)]
- active state (A,TimeStamp = i) is set 
- SPE driver takes (A,i) and returns set of set SuperS = {S1, S2,..., Sn} where dynamics will be allowed to take place [This is taken as an argument by the function]
- (SuperS, i) is recorded in the SPE Record [maybe as a dictionary] [this is kept in a time_step function for stepping through time]
- graph dynamics engine takes (A,i) and SuperS and returns SuperChanges = {C1, C2, C3... ,Cn} representing changes in attributes and additional or removed edges 
- SuperChanges is fed to a change driver which returns a new active graph (A, i+1)
- also need an graph history? I can't remember if thats inherrant in the dynagraph type 
#---------------------------------------------------------#

- time_step 
    - does the actions in a single time step calls SuperS
    - records everything 
    - gets the changes
    - calls the change to the active graph 

- timestepper 
    - initialises records 
    - then calls time_step as many times as decided 

- SuperS is outputted by the SPE driver 
- the dynamic should act on a single element of SuperS and return what it would 

**FINALISED ELEMENTS** 
- Graph initialisation program 
- Active graph 
- SPE driver 
- SuperS (subsets of the active graph) 
- SPERecord 
- graph dynamics engine 
- SuperChanges (set of changes to the graph) 
- ChangeDriver 

**TODO** 

- Need to code tests for all basic inputs
- the inputs of the class is 
    - self 
    - graph dynamics engine 
        - random rewiring 
        - complete graph insertion 
        - toggling all edges on to off 
        - add 1 or minus 1 to all edge weights 
    - init conditions ( I think these are all included in netex)
        - empty graph 
        - complete graph 
        - erdoss renyi graph 
    - SPE driver 
        - random samples (taken using bernoulli on the nodes)
        - randomly chosen with fixed size 
        - random but weighted using node degree 
        - etc 
    - end time 

**NOTE** 

- apply the dynamic to the subgraph to get the target subgraph and then you can use the networkX difference function in order to find the stuff that needs to be changed. This doesnt work with attributes 
- annoyingly dynetx just doesnt work in the way I want it to. It wants to be fed a dynamic graph set of snapshots. Then it can play them back or use nice algorithms or analyse it a reasonably smart way. It can't be used to add or remove edges in the way I want. There are 2 possible paths 
    1. edit the functions within dynetex to allow adhoc edge removal 
    2. keep a historic record of edge additions/ attribute changes and a current networkx graph which can act as a place for our dynamics to take place. This is definitely not ideal but I'm too lazy to do 1 

