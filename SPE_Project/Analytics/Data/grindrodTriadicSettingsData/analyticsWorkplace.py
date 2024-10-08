import numpy as np
import matplotlib.pyplot as plt

from edgeDensityCalc import edge_density

density_dict = {}
for i in range(4): 
    file_name = 'grindrodTriadicSettingsFile' + str(i) +'.txt'
    density_dict[i] = edge_density(file_name)



# Create an index array
indexes = np.arange(len(density_dict[0]))

# Plot the arrays
plt.plot(indexes, density_dict[0], label='Array 1')
plt.plot(indexes,density_dict[1], label='Array 2')
plt.plot(indexes, density_dict[2], label='Array 3')
plt.plot(indexes,density_dict[3], label='Array 4')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

# Show the plot
plt.show()
