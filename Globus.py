import matplotlib.pyplot as plt                                 # risanje
import cartopy.crs as ccrs                                      # projekcija
import cartopy.feature as cfeature                              # relief
from matplotlib.animation import FuncAnimation                  # animacija
from matplotlib.offsetbox import OffsetImage, AnnotationBbox    # dodajanje lokacije
import numpy as np                                              # numerika

# Definirane/izbrane lokacije
lokacije = [
    
    # Severna vzhodna polobla
    {'ime': 'Tokyo', 'lat': 35.68, 'lon': 139.77},
    {'ime': 'Berlin', 'lat': 52.52, 'lon': 13.41},
    {'ime': 'Reykjavik', 'lat': 64.13, 'lon': -21.82},
    {'ime': 'Praga', 'lat': 50.09, 'lon': 14.42},     

    # Severna zahodna polobla
    {'ime': 'Alert', 'lat': 82.50, 'lon': -62.33},
    {'ime': 'Denver', 'lat': 39.74, 'lon': -104.99},
    {'ime': 'Toronto', 'lat': 43.70, 'lon': -79.42},

    # Južna vzhodna polobla
    {'ime': 'Sydney', 'lat': -33.87, 'lon': 151.21},
    {'ime': 'McMurdo_Station', 'lat': -77.85, 'lon': 166.67},
    {'ime': 'Auckland', 'lat': -36.85, 'lon': 174.76},
    
    # Južna zahodna polobla
    {'ime': 'Santiago', 'lat': -33.45, 'lon': -70.67},
    {'ime': 'Lima', 'lat': -12.05, 'lon': -77.03},
]

# Rdeča pika
def rdeca_pika():
    fig, ax = plt.subplots(figsize=(0.1, 0.1), dpi=100) # velikost
    ax.scatter([0.5], [0.5], s=100, color='red') # definiramo obliko
    ax.set_xlim(0, 1) # relativna lokacija
    ax.set_ylim(0, 1)
    ax.axis('off') # Odstrani koordinatni sistem na sliki
    fig.canvas.draw()
    image = np.array(fig.canvas.renderer.buffer_rgba())
    plt.close(fig)
    return image

# Ustvarimo figuro za animacijo
fig = plt.figure(figsize=(10, 5))

pika = rdeca_pika()

# Preverjanje vidnosti na globusu glede na os vrtenja
def vidnost(lon, lat, central_lon):
    lon_diff = (lon - central_lon + 180) % 360 - 180
    return abs(lon_diff) < 90 and abs(lat) < 90

# Posodabljanje animacije
def update(frame):
    # Počisti prejšnjo figuro
    fig.clear()
    # Ustvari novo projekcijo poloble, ji doda relief
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(central_longitude=frame, central_latitude=0.0))
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE)
    
    # Vidne lokacije označi z imenom in piko
    for lokacija in lokacije:
        if vidnost(lokacija['lon'], lokacija['lat'], frame):
            # Doda rdečo piko (zoom = velikost pike)
            ab = AnnotationBbox(OffsetImage(pika, zoom=0.5), (lokacija['lon'], lokacija['lat']),
                                xycoords=ccrs.PlateCarree()._as_mpl_transform(ax), frameon=False)
            ax.add_artist(ab)

            # Doda ime lokacije, zamakne tiste, ki se prekrivajo
            if lokacija['ime'] in ['Praga', 'Auckland', 'Denver']:
                lat_offset = -10
            elif lokacija['ime'] == 'Alert':
                lat_offset = 5
            else:
                lat_offset = 0
            ax.text(lokacija['lon'] + 5, lokacija['lat'] + lat_offset, lokacija['ime'],
                    transform=ccrs.PlateCarree(), fontsize=13, color='black',
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='black'))
    return [ax] # vrne figuro trenutno vidne poloble

# Ustvari animacijo, kliče update za vsak frame, .linspace() določa število korakov
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 115), interval=90, blit=False)

# Shrani animacijo kot gif
ani.save("globus.gif", writer="pillow")

# Zapre figuro
plt.close(fig)