import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import netCDF4
from matplotlib.colors import Normalize #for color bar 
import geopandas

#read Crop_yield
filename = 'YLD_Ref.run01_O3_IRR_1st_2020.nc'
ncdata = netCDF4.Dataset(filename, 'r', format='NETCDF4')
C = ncdata.variables['Crop_yield'][:]

#test
print( 'variables in nc file:',ncdata.variables.keys())

#figure
fig = plt.figure()
#C = np.ma.masked_where(C<-100, C)
#C = np.log(C+1)
vma = np.max(C)
vmi = np.min(C)
print(vma,vmi)
#C = np.ma.masked_where(C<0, C)
cm = plt.cm.get_cmap('Greens')
ax = fig.add_subplot(111)
im = ax.imshow(C, cmap=cm, origin='lower', norm=Normalize(vmin=vmi, vmax=17500))
#ax.set_xlabel('longitude')
#ax.set_ylabel('latitude')
fig.colorbar(im, label='Crop_yield(kg/ha)', orientation='horizontal')

#cont=plt.contour(C<-100,colors='black')
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot(edgecolor='#444', facecolor='white', linewidth = 0.5)


plt.show()
