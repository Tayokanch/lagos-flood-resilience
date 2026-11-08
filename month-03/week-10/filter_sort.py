import pandas as pd
import os

dir = 'data'
sub_dir = 'raw'

file_path = os.path.join(dir, sub_dir, 'ward_population.csv')

pop = pd.read_csv(file_path)

big = pop[pop['population_2024'] > 35000]

print(big.head());

print(f'There are {len(big)} wards with a population greater than 35,000')

## Sorting the data by population in descending order and displaying the top 3 wards
rank = pop.sort_values('population_2024', ascending=False)
print(rank.head(3))

pop['population_thousands'] = pop['population_2024']/1000
print(pop.head(3))

print('Total Population:', pop['population_2024'].sum())