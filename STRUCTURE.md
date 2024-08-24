
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
