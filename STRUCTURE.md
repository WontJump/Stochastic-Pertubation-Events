# elements 
- graph dynamics engine 
- active graph 
- spe driver 
- initial graph state 
- graph visualisation 

- active graph should be completely controlled within DyNetX 
- graph visualisation can be handled by a Dynetex object augmented with the SPE happening at that time step 
    - Need a dictionary of SPE's keyed by timestamp 

# Programming the active graph 
--> (a depends on b) 

- active graph initialised with initial graph state default null 
- spe driver then decides which spe to activate and the time stamp 
- spe driver --> previous active state 
- once spe driver defines the spe then pass to the graph dynamics engine 
- graph dynamics engine then updates the active graph with the new edges and attributes so 

# Pipe line 

- Graph initialised 
- active state (A,TimeStamp = i) is set 
- SPE driver takes (A,i) and returns set of set SuperS = {S1, S2,..., Sn} where dynamics will be allowed to take place 
- (SuperS, i) is recorded in the SPE Record [maybe as a dictionary]
- graph dynamics engine takes (A,i) and SuperS and returns SuperChanges = {C1, C2, C3... ,Cn} representing changes in attributes and additional or removed edges 
- SuperChanges is fed to a change driver which returns a new active graph (A, i+1)

**FINALISED ELEMENTS** 
- Graph initialisation program 
- Active graph 
- SPE driver 
- SuperS (subsets of the active graph) 
- SPERecord 
- graph dynamics engine 
- SuperChanges (set of changes to the graph) 
- ChangeDriver 
