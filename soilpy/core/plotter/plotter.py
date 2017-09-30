import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    """
    The plotter class.
    """

    def __init__(self, soil_profile):
        self.soil_profile = soil_profile

    def plot_level_list(self, list, plot_values=True):
        y = np.array(self.soil_profile.level_list).flatten()
        plt.plot(list, y)
        if(plot_values):
            for a, b in zip(list, y):
                plt.text(a, b, str(a))