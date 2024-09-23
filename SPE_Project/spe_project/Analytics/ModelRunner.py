from pathlib import Path
data_path = '/home/wont-jump/Documents/GitHub/Stochastic-Pertubation-Events/SPE_Project/spe_project/Analytics/Data'

def bulk_create(
        SPEModel,
        bulk_size, 
        file_name,
        file_path = None
        ):
    
    if file_path: 
        current_directory = Path(file_path) 
    else: 
        current_directory = Path.cwd()

    dir_name = file_name + 'Data'
    new_directory = current_directory / dir_name
    new_directory.mkdir(parents=True, exist_ok=True)

    for i in range(bulk_size): 
        current_file_name = file_name + 'File' + str(i) + '.txt'
        path = new_directory / current_file_name
        path = str(path)
        SPEModel.timestepper()
        SPEModel.file_record(path)

