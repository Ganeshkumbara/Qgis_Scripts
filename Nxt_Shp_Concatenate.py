import os
import geopandas as gpd

# reference site
# https://spatial-dev.guru/2022/06/05/merging-multiple-shapefiles-into-one-shapefile-using-python-and-geopandas/
# path were shp files r loaded

Sh_file_loaded_path = 'C:\\Py_projects\\Qgis_Scripts\\shp_merge\\output'
files_list = os.listdir(Sh_file_loaded_path)


shp_dicto = {}

for file in files_list:
    if file.endswith('master_strings.shp'):
        file_path = Sh_file_loaded_path + '\\' + file
        shp_file = gpd.read_file(file_path)
        update = shp_dicto.get('shp',[]) 
        update.append(shp_file)
        shp_dicto['shp'] = update

# merge individual Shp files .concat takes list as argument
merged_shp = gpd.pd.concat(shp_dicto['shp'])

output_path = os.path.join(Sh_file_loaded_path,'Merged')

# check if path is there
if  os.path.exists(output_path):
    pass
else:
    os.makedirs(output_path)


# save merged file
merged_shp.to_file(output_path+'\\'+'master_strings.shp')



        
   
