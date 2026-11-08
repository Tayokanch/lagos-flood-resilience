import geopandas as gpd
import pandas as pd 
import os 


dir = 'data'
sub_dir = 'raw'
filename = 'health_facilities.csv'
file_path = os.path.join(dir, sub_dir, filename)
output_path = os.path.join(dir, 'processed', 'facilities.gpkg')

table = pd.read_csv(file_path)

print(table.head(3))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table.longitude, table.latitude),
    crs='EPSG:4326'
)

print(facilities.head(3))
print(facilities.crs)

facilities.to_file(output_path, layer='facilities')

print('Saved,', len(facilities), 'facilities')
