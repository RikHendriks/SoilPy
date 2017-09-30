import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    """
    The plotter class.
    """

    def __init__(self, soil_profile):
        self.soil_profile = soil_profile

    def plot_level_list(self, x, plot_values=True):
        y = self.soil_profile.level.get_numpy_array()
        plt.plot(x, y)
        if(plot_values):
            for a, b in zip(x, y):
                plt.text(a, b, str(a))