# Qgis_Scripts

Master.py 

Master script take path and jsons as inputs and perform action on the selected jsons, actions listed below:

1: Remove Module Number
2: Remove Temperature 
3: Remove temp for missing module
4: Remove string number

workflow : 
 * As the script executed user get a list of actions and jsons files (Json listed from the current folder where Script file located )
 * Each json will go through validator function to get validated for selected action field present in it; if not validated it will get ignored  
 * selected action will be perfomed on the selected jsons
 * Modified Json files will get saved in output folder, output folder named after selected action

 
Nxt_shape_concatenate.py

* Scipt take path as input
* script will loop through individual folder and concate master_string.shp and string.shp seperatly 

