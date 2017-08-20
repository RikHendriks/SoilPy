import pytest
from soilpy import *

def test_stress_tensor():
    s = Soil(15, 18)
    wl = WaterLayer(0)
    sl = SoilLayer(s, wl, 0, -5)
    assert True

def test_effective_stress_tensor():
    s = Soil(15, 18)
    wl = WaterLayer(0)
    sl = SoilLayer(s, wl, 0, -5)
    assert True

def test_vertical_normal_stress():
    s = Soil(15, 18)
    wl = WaterLayer(-3)
    sl = SoilLayer(s, wl, 0, -5)
    assert sl.vertical_normal_stress(0) == 0
    assert sl.vertical_normal_stress(-2) == -30
    assert sl.vertical_normal_stress(-3) == -45
    assert sl.vertical_normal_stress(-5) == -81
    # Test if the exceptions are thrown.
    with pytest.raises(ValueError) as excinfo:
        sl.vertical_normal_stress(1)
    assert str(excinfo.value) == "The given level=1 is not between the top level t=0 and the bottom level b=-5"
    with pytest.raises(ValueError) as excinfo:
        sl.vertical_normal_stress(-6)
    assert str(excinfo.value) == "The given level=-6 is not between the top level t=0 and the bottom level b=-5"

def test_vertical_water_pressure():
    # waterlayer is above the top layer
    s = Soil(15, 18)
    wl = WaterLayer(2)
    sl = SoilLayer(s, wl, 0, -5)
    assert sl.vertical_water_pressure(0) == -20
    assert sl.vertical_water_pressure(-3) == -50
    assert sl.vertical_water_pressure(-5) == -70
    # waterlayer is in between the layers
    s = Soil(15, 18)
    wl = WaterLayer(-3)
    sl = SoilLayer(s, wl, 0, -5)
    assert sl.vertical_water_pressure(0) == 0
    assert sl.vertical_water_pressure(-2) == 0
    assert sl.vertical_water_pressure(-3) == 0
    assert sl.vertical_water_pressure(-5) == -20
    # Test if the exceptions are thrown.
    with pytest.raises(ValueError) as excinfo:
        sl.vertical_water_pressure(1)
    assert str(excinfo.value) == "The given level=1 is not between the top level t=0 and the bottom level b=-5"
    with pytest.raises(ValueError) as excinfo:
        sl.vertical_water_pressure(-6)
    assert str(excinfo.value) == "The given level=-6 is not between the top level t=0 and the bottom level b=-5"

def test_vertical_water_pressure_different_water_pressures():
    # waterlayer is above the top layer
    s = Soil(15, 18)
    wl = WaterLayer(2)
    wll = WaterLayer(-2)
    sl = SoilLayer(s, wl, 0, -5)
    assert sl.vertical_water_pressure(0, wll) == 20
    assert sl.vertical_water_pressure(-4, wll) == 10
    assert sl.vertical_water_pressure(-5, wll) == -30
    # waterlayer is in between the layers
    s = Soil(15, 18)
    wl = WaterLayer(-3)
    wll = WaterLayer(-2)
    sl = SoilLayer(s, wl, 0, -5)
    assert sl.vertical_water_pressure(-3, wll) == 0
    assert sl.vertical_water_pressure(-4, wll) == -15
    assert sl.vertical_water_pressure(-5, wll) == -30

def test_effective_vertical_normal_stress():
    s = Soil(15, 18)
    wl = WaterLayer(-3)
    sl = SoilLayer(s, wl, 0, -5)
    assert sl.effective_vertical_normal_stress(0) == 0
    assert sl.effective_vertical_normal_stress(-2) == -30
    assert sl.effective_vertical_normal_stress(-3) == -45
    assert sl.effective_vertical_normal_stress(-5) == -61
    # Test if the exceptions are thrown.
    with pytest.raises(ValueError) as excinfo:
        sl.effective_vertical_normal_stress(1)
    assert str(excinfo.value) == "The given level=1 is not between the top level t=0 and the bottom level b=-5"
    with pytest.raises(ValueError) as excinfo:
        sl.effective_vertical_normal_stress(-6)
    assert str(excinfo.value) == "The given level=-6 is not between the top level t=0 and the bottom level b=-5"