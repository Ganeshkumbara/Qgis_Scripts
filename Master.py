import inquirer
import json
import os
from colorama import Fore, Style


questions = [

  inquirer.List('action',
                message="Choose the action to be performed",
                choices=['Remove_Module_number', 'Remove_Temperature', 'Remove_Temp/Missing_module', 'Remove_String_numbers'],
            ),
]

user_choice = inquirer.prompt(questions)['action']

class Terminator:
    def __init__(self, path):
        self.current_dir = path
        self.dir_list = os.listdir(self.current_dir)
        self.json_dir_list = []
        for files in self.dir_list:
            if files.endswith('.json'):
                self.json_dir_list.append(files)
        

    def mn_remove(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
            validator = 0

            for feature in features:
                if feature['properties']['class_name'] == 'table' :
                    continue
                else:
                    '''Remove Module Number'''
                    string_number = feature['properties']['string_number'] 
                    split = string_number.split('-')
                    Module_number = split[-2:]
                    
                    '''check if module number are there in string numbers'''
                    if Module_number[0].startswith("R") or Module_number[0].startswith("C"):
                        string = ''
                        for num in Module_number:
                            string = string+'-'+num
                            string_numbers = string_number.replace(string,'')
                            feature['properties']['string_number'] = string_numbers
                            validator += 1
                    else:
                        continue
            if validator > 0:
                template = {'type':"FeatureCollection",'name':'pl2','features':features} 
                path = file_path.replace('.json','_module_number_removed.json')
                with open(path, 'w') as f:
                    json.dump(template,f)
                print(Fore.GREEN + f'Module_number_removed sucessfully for {file} ... '+ Fore.RESET)
            else:
                print(Style.BRIGHT + Fore.RED + f'Module_numbers r not updated for {file}'+Fore.RESET)
        # print('Module_number_removed sucessfully... ')
    
    def Temp_remove(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
    
            for feature in features:
                if feature['properties']['class_name'] == 'table' :
                    continue
                else:
                    '''Remove Temperature '''
                    temp = feature['properties']['temperature_difference']
                    temp = 0
                    feature['properties']['temperature_difference'] = temp

            template = {'type':"FeatureCollection",'name':'pl2','features':features} 
            path = file_path.replace('.json','_temperature_removed.json')
            with open(path, 'w') as f:
                json.dump(template,f)
        print('Temperature_removed sucessfully... ')

    def Missing_module_temp(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
            validator  = 0

            for feature in features:
                if feature['properties']['class_name'] != 'missing_module' :
                    continue
                else:
                    '''Remove Temperature '''
                    temp = feature['properties']['temperature_difference']
                    temp = 0
                    validator += 1
                    feature['properties']['temperature_difference'] = temp
            if validator > 0:
                template = {'type':"FeatureCollection",'name':'pl2','features':features} 
                path = file_path.replace('.json','_Missing_temp_removed.json')
                with open(path, 'w') as f:
                    json.dump(template,f)
            else:
                continue
        print('Missing_module_temperature_removed sucessfully... ')

    def string_remove(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
    
            for feature in features:
                if feature['properties']['class_name'] == 'table' :
                    continue
                else:
                    '''Remove Temperature '''
                    string_numbers = feature['properties']['string_number']
                    string_numbers = None
                    feature['properties']['string_number'] =  string_numbers

            template = {'type':"FeatureCollection",'name':'pl2','features':features} 
            path = file_path.replace('.json','_string_number_removed.json')
            with open(path, 'w') as f:
                json.dump(template,f)
        print('String_number_removed sucessfully... ')




path =  os.getcwd()

obj = Terminator(path)

dicto = {'Remove_Module_number': obj.mn_remove, 'Remove_Temperature':obj.Temp_remove,
          'Remove_Temp/Missing_module': obj.Missing_module_temp, 'Remove_String_numbers':obj.string_remove}

dicto[user_choice]()






