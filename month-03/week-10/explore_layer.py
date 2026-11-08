import geopandas as gpd
import os 

dir = 'data'
sub_dir = 'processed'
filename = 'wards.gpkg'
file_path = os.path.join(dir, sub_dir, filename)

print(gpd.list_layers(file_path))

wards = gpd.read_file(file_path, layer='wards')

print(wards.head())

print('Rows and Columns count :', wards.shape)

## Print each column geometry type
print(wards.geom_type)

## Print column geometry type count

print(wards.geom_type.value_counts())

print('CRS:', wards.crs)

## Print the bounds of the GeoDataFrame
print('Bounds:', wards.total_bounds)