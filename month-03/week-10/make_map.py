import geopandas as gpd
import os
import matplotlib.pyplot as plt

wards_path = os.path.join('data', 'processed', 'wards.gpkg')

facilities_path = os.path.join('data', 'processed', 'facilities.gpkg')

wards = gpd.read_file(wards_path, layer='wards')
facilities = gpd.read_file(facilities_path, layer='facilities')

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color='#E6F2F3', edgecolor='#037E8A')
facilities.plot(ax=ax, color='#094923', markersize=18)
ax.set_title('Health Facilities In Ibadan North')
ax.set_axis_off()

fig.savefig('month-03/week-10/facilities_map.png', dpi=150, bbox_inches='tight')
print('Map Saved');
