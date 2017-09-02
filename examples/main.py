from soilpy import *

water_level = WaterLayer(-1)

sand = Soil(18, 20)
clay = Soil(17, 17)

s_m = SoilManager()
s_m.add_soil_layer(SoilLayer(sand, water_level, 0, -2))
s_m.add_soil_layer(SoilLayer(clay, water_level, -2, -4))
s_m.add_soil_layer(SoilLayer(sand, water_level, -4, -10))

data = SoilMechanicsData()

s_m.process_function(calculate_water_pressure, data)
s_m.process_function(calculate_vertical_normal_stress, data)
s_m.process_function(calculate_effective_vertical_normal_stress, data)

print(data)