import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    """
    The plotter class.
    """

    def __init__(self, soil_profile):
        self.soil_profile = soil_profile

    def plot_level_list(self, x, plot_values=True):
        """
        Plots a List in the SoilProfileData class.
        :param x: A ProfileList.
        :param plot_values: If the values need to be plotted.
        """
        x = x.get_numpy_array()
        y = self.soil_profile.level.get_numpy_array()
        plt.plot(x, y)
        if(plot_values):
            for a, b in zip(x, y):
                plt.text(a, b, str(a))