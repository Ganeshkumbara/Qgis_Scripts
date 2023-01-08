# Qgis_Scripts

Master.py 

Master file take path and jsons as input perform action on jsons actions like:
1: Remove Module Number
2: Remove Temperature 
3: Remove temp for missing module
4: Remove string number

workflow : 
 * as script excuted user get a list of actions and a list of jsons file in current folder(Where master.py file loacated)
 * selected action will be perfomed on the selcted jsons
 * Mastery.py validate the json for a give action all requirement r there in json. if not it will ignore the json file and go fo the next one
 
Nxt_shape_concatenate.py

script will loop through individual folder and concate master_string.shp and string.shp seperatly 

