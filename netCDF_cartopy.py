import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import datetime
import netCDF4
from matplotlib.colors import Normalize #for color bar 


#prepare data
nx, ny = 720, 360
west, east, south, north = 0, 360, -90, 90
#west, east, south, north = -180, 180, -90, 90
lons = np.linspace( west+180./nx, east-180./nx, nx)
lats = np.linspace( south+90./ny, north-90./ny, ny)
#lons[lons > 180] -= 360              ## The west latitude must be negative

# Show the map
fig = plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=360.0))
ax.add_feature(cfeature.LAND)
ax.coastlines()
ax.gridlines()

#read Crop_yield
filename = 'YLD_Ref.run01_O3_IRR_1st_2020.nc'
ncdata = netCDF4.Dataset(filename, 'r', format='NETCDF4')
C = ncdata.variables['Crop_yield'][:]
#C = np.ma.masked_where(C<-100, C)
#C = np.log(C+1)
vma = np.max(C)
vmi = np.min(C)
print(vma,vmi)
#C = np.ma.masked_where(C<0, C)
cm = plt.cm.get_cmap('Greens')

#show the data
#m.imshow(C, cmap=cm, origin='lower', norm=Normalize(vmin=vmi, vmax=17500))
im = ax.imshow(C, transform=ccrs.PlateCarree(), cmap=cm, origin='lower', norm=Normalize(vmin=vmi, vmax=17500))

#ax.set_xlabel('longitude')
#ax.set_ylabel('latitude')

plt.colorbar(im, aspect=50,pad=0.08,orientation='horizontal')
#m.colorbar(im, label='Crop_yield(kg/ha)', orientation='horizontal')

ax.set_title('Crop_yield[kg/ha]')
