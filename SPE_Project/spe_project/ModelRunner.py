from pathlib import Path
import time 
data_path = '/home/wont-jump/Documents/GitHub/Stochastic-Pertubation-Events/SPE_Project/spe_project/Analytics/Data'

def bulk_create(
        SPEModel,
        bulk_size, 
        file_name,
        file_path = None
        ):
    """
    bulk_create(function) runs a single SPEModel multiple times and stores the resultant files in a designated
    folder 
    
    :param SPEModel: a model defined in GraphSPEModel.py
    :param bulk_size: the number of times you want to run SPEModel
    :param file_name: name of the files to be created 
    :param file_path: alternative filepath to save new files to  
    """
    
    if file_path: 
        current_directory = Path(file_path) 
    else: 
        current_directory = Path.cwd()

    dir_name = file_name + 'Data'
    new_directory = current_directory / dir_name
    new_directory.mkdir(parents=True, exist_ok=True)

    # just a quick timing run to give me an idea of how long I should wait 

    start_time = time.time() 
    current_file_name = file_name + 'File' + str(1) + '.txt'
    path = new_directory / current_file_name
    path = str(path)
    SPEModel.timestepper()
    SPEModel.file_record(path)
    end_time = time.time() 

    print(f"Predicted execution time: {(end_time - start_time)*(bulk_size - 1)} seconds")

    for i in range(bulk_size - 1): 
        current_file_name = file_name + 'File' + str(i) + '.txt'
        path = new_directory / current_file_name
        path = str(path)
        SPEModel.timestepper()
        SPEModel.file_record(path)