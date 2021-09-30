import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
data = gpd.read_file('Hex_grid/isea3h7.shp')

np.set_printoptions(np.inf)
print(data[0:1])
#4colums

richnessMigraBRsimu = np.loadtxt('richnessMigraBRsimu.txt')
richnessMigraBRsimu = np.log(richnessMigraBRsimu + 1)
data['richnessMigraBRsimu'] = richnessMigraBRsimu[:]

print(data[0:1])
#5colums

data.plot(column='richnessMigraBRsimu', cmap='jet', vmax=6, legend=True, legend_kwds={'label': "ln(Number of species + 1)", 'orientation': "horizontal"})
plt.show()
