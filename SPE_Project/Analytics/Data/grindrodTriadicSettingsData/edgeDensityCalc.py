from collections import defaultdict, Counter
import numpy as np 
import math 

def edge_density(datafile): 
    '''
    :param datafile: .txt file with data in the 001 format 

    I was having some really weird bugs when writing this and I should check it over just incase something remains 
    '''
    with open(datafile, 'r') as f: 
        file_format = next(f)

        # if file_format != 'file format 001':
        #     raise Exception('wrong file format: only accepted format is 001') #this was throwing rougue errors 
        next(f) 

        history = {}
        for line in f:


            if line.strip(): 
                
      
                line_split = line.split()
                if len(line_split) == 1 : 
                    node_num = int(line.strip())
                    continue 
  
                sign = line_split[2]
                time = line_split[3]


                if time in history: 
                    history[time] = history[time] + [sign]
                else: 
                    history[time] = [sign]



    
    history_net = []
    history_run = []

    max_edges = math.comb(node_num, 2)
   
    for i in history: 
        history[i] = Counter(history[i])
        history_net.append(history[i]['+'] - history[i]['-'])
        j = int(i)
        history_run.append(sum(history_net[:j])) # I believe the index of the file follows standard python indexing
    
    return np.array(history_run) / max_edges 






