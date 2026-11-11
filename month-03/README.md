# Month 3: Geospatial Python and Automation

- ## Week 10 : Geopandas, layers as tables
  
    ## What this folder contains
    - **explore_pandas.py**: This is a script to look or explore the ward_population.csv file using pandas
  
    - **explore_layer.py**: Used geopandas to read a geopackage file (wards.gpkg)[wards.gpkg]: Explore a Geodataframe Data stucture and the difference btw an ordinary Dataframe, determined the `first 5 rows`, `geometry type`, it `crs` 
  
    - **join_population.py**: This script is for performing attribute join using a 2 different file (wards.gpkg)[wards.gpkg] and (ward_population.csv)[ward_population.csv] with their common attribute
  
    - **save_outputs.py**: This file contains a script where geopandas was used to read a geopackage file , dropped the geometry column and saved the output as a csv file
  
    - **make_map.py**: Contains a script where geopandas and matplotlib as used to plot health facilities corresponding each eards in Ibadan North

    ## What I found
    
    - I could geopaandas or pandas to perform a task on a column without having to iterate on each cell
    - I could perform almost all the spatial analysis concept on Qgis usig Python libraries like pandas, geopandas e.t.c