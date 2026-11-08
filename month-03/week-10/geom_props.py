import geopandas as gpd
import os 


dir = 'data'
sub_dir = 'processed'
filename = 'wards.gpkg'
file_path = os.path.join(dir, sub_dir, filename)

wards = gpd.read_file(file_path, layer='wards')

first = wards.geometry.iloc[0]

print(type(first))

print(first)

## Checks if the geometry is valid / well formed
 
print('Valid:', first.is_valid)

## Print the centre point of the geometry

print('Centroid', first.centroid)