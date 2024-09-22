import matplotlib.pyplot as plt
import networkx as nx

class ModelVis:

    def __init__(self, model):
        """
        Constructor to make ModelVis object. Nothing will be displayed by calling the constructor alone.
        By default will draw graph at it's final state
        :param model: GraphSPEModel object
        """
        self.model = model
        self.num_timesteps = len(self.model.SPE_dict)
        self.timestep = self.num_timesteps - 1


    def show(self):
        """
        Draws the graph at the current time we are looking at
        """
        nx.draw(self.model.active_graph)
        plt.show()

    def go_to_timestep(self, timestep, show=True):
        """
        :param timestep: (unsigned int) Time to go to
        :param show: (bool=True) Whether to call self.show() or not
        """
        # TODO
        pass

    def jump_forward(self):
        """
        Go forward 1 time step so the graph will be drawn at it's next state
        :return: (Bool) Is the graph now at its final state?
        """
        # TODO
        pass

    def jump_back(self):
        """
        Go back 1 time step so the graph will be drawn at its previous state
        :return: (Bool) Is the graph now at its initial state?
        """
        # TODO
        pass
