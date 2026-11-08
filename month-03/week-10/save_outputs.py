import geopandas as gpd
import os

wards_path = os.path.join('data', 'processed', 'wards.gpkg')

output_file =  os.path.join('data', 'processed', 'week10_outputs.gpkg')

wards = gpd.read_file(wards_path)

wards.to_file(output_file, layer='wards_copy')

## drop the grometry column and save the file as a csv to with the given name
wards.drop(columns='geometry').to_csv('month-03/week-10/wards_table.csv', index=False)

print(gpd.list_layers(output_file))
