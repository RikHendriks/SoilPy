from soilpy import *

import matplotlib.pyplot as plt

water_level = WaterLayer(1)

sand = Soil(18, 20, 30)
clay = Soil(17, 17, 35)

s_p = SoilProfile("n")
s_p.add_soil_layer(SoilLayer(sand, water_level, 0, -2))
s_p.add_soil_layer(SoilLayer(clay, water_level, -2, -4))
s_p.add_soil_layer(SoilLayer(sand, water_level, -4, -10))

data = SoilProfileData()

s_p.process_soil_mechanics(data)

# print(data)

l = np.array(data.level_list).flatten()
w = np.array(data.water_pressure_list).flatten()
v = np.array(data.vertical_normal_stress_list).flatten()
ev = np.array(data.effective_vertical_normal_stress_list).flatten()


def plot_levels(x, y):
    plt.plot(x, y)
    for a, b in zip(x, y):
        plt.text(a, b, str(a))


plot_levels(w, l)
plot_levels(v, l)
plot_levels(ev, l)

plt.show()