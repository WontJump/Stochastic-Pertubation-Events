from typing import Any


class SPE_defined_sequence: 

    def __init__(self,alias_driver_dict, event_list): 
        """
        the use case of this is: suppose we have two drivers A, B and we want to apply the first 4 times and the
        second 5 times or perhaps in a sequence A,B,A,A,B,A this gives a way of doing this efficiently 

        :param alias_driver_dict: gives a dictionary where keys are the aliases used in events list
        and values are the drivers the aliases refer to 

        :param event_list: gives the order in which the drivers should be applied  
        """  
        self.alias_driver_dict = alias_driver_dict
        self.event_list = event_list

    def __call__(self, G, i): 
        current_alias = self.event_list[i] #check indexing! 
        return self.alias_driver_dict[current_alias](G,i) 
    
class SPE_driver_combine: 
    def __init__(self, driver_duration_list): 
        """
        this is meant to speed up the use case defined above where you want to run A n times and B m times 
        this will automatically generate aliases and a sequence AAAA... BBBB... and then call SPE_defined_sequence 
        I'm worried that this will be slower than it could be and more memory heavy than it could be. REVIEW 

        :param driver_duration_list: a list of tuples of the form (driver, duration) 
        """
        driverDict = {}
        eventList = [] 

        for i in range(driver_duration_list):
            eventList += [i for j in range(driver_duration_list[i][1])]
            driverDict[i] = driver_duration_list[i][0]

        self.combined_driver = SPE_defined_sequence(driverDict, eventList)

    def __call__(self,G,i): 
        self.combined_driver(G,i)



        

