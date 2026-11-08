import os
import pandas as pd
import geopandas as gpd


wards_file_path = os.path.join('data', 'processed', 'wards.gpkg')
pop_file_path = os.path.join('data', 'raw', 'ward_population.csv')

wards = gpd.read_file(wards_file_path, layer='wards')
pop = pd.read_csv(pop_file_path)

## Join population table using ('ward') to wards using ('ward_name') both field have common value

first_try = wards.merge(pop, left_on='ward_name', right_on='ward', how='left')
matched = first_try['population_2024'].notna().sum()

print('Matched on first try:', matched, len(wards))

def clean_name(name):
    return name.strip().upper().replace('-', ' ')


wards['join_key'] = wards['ward_name'].apply(clean_name)
# Create a new column 'join_key' in the wards GeoDataFrame
# and apply the clean_name function to each value in wards['ward_name'].

pop['join_key'] = pop['ward'].apply(clean_name)

# Create a new column 'join_key' in the pop GeoDataFrame
# and apply the clean_name function to each value in wards['ward'].


joined = wards.merge(pop, on='join_key', how='left')
print(joined)

matched = joined['population_2024'].notna().sum()

print('Matched on after cleaning:', matched, len(wards))

print(joined[['ward_name', 'population_2024']])
print('This is wards',wards.columns)
