import inquirer
import json
import os
from colorama import Fore, Style

current_dir = os.getcwd()
files_list = os.listdir(current_dir)

questions = [

  inquirer.List('action',
                message="Choose the action to be performed",
                choices=['Remove_Module_number', 'Remove_Temperature', 'Remove_Temp/Missing_module', 'Remove_String_numbers'],
            ),
  inquirer.Checkbox('select_files',
                    message="What are you interested in?",
                    choices = [file for file in files_list if file.endswith('.json')],
                  )          
]

answer = inquirer.prompt(questions)

actions = answer['action']
selected_jsons = answer['select_files']


class Terminator:
    def __init__(self, path, selected_jsons):
        self.current_dir = path
        self.json_dir_list =  selected_jsons
        self.output_file = path +'\\'
        
        
    '''check action field exists in json'''
    def check_feild(self, issue, json_file, field):
        try:
            issue['properties'][field]
        except KeyError :
            print((Fore.RED + f'{field} field not exists in : {json_file}' + Fore.RESET))
            return False
        return True
     
       
    def module_number(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
            output = self.output_file + 'Module_nor_removed'
            action_field = 'string_number'
            validator = ''

            for feature in features:  
                if feature['properties']['class_name'] == 'table' :
                    continue
                else:
                    # '''Check if string number field exists in current feature'''
                    if self.check_feild(feature, file, action_field):
                        string_number = feature['properties'][action_field] 
                        split = string_number.split('-')
                        Module_number = split[-2:]

                        # '''check if module number are there in string numbers'''
                        if Module_number[0].startswith("R") or Module_number[0].startswith("C"):
                            string = ''
                            for num in Module_number:
                                string = string+'-'+num
                            
                            string_numbers = string_number.replace(string,'')
                            feature['properties']['string_number'] = string_numbers
                            validator = 'module_exist'
                                
                        else:
                            validator = 'module_not_exist'
                            continue
                    
                    else:
                        break
                       
            '''create new json file if module number removed else ignore '''      
            if validator == 'module_exist':
                template = {'type':"FeatureCollection",'name':'pl2','features':features} 
                path = output + '\\' + file + '.json'

                if not os.path.exists(output):
                    os.makedirs(output)
                with open(path, 'w') as f:
                    json.dump(template,f)
                print(Fore.GREEN + f'Module_number_removed successfully : {file}'+ Fore.RESET)
            elif validator == 'module_not_exist':
                print(Fore.RED + f'Module_numbers not exists in string number : {file}'+Fore.RESET)
        

    def Temp_remove(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
            output = self.output_file + 'Temperature_removed'
            action_field = 'temperature_difference'
            validator = False

            for feature in features:
                if feature['properties']['class_name'] == 'table' :
                    continue
                else:
                    '''Remove Temperature '''
                    if self.check_feild(feature, file, action_field):
                        temp = feature['properties']['temperature_difference']
                        temp = 0
                        feature['properties'][action_field] = temp
                        validator = True
                    else:
                        break
            if validator:
                template = {'type':"FeatureCollection",'name':'pl2','features':features} 
                path = output + '\\' + file + '.json'

                if not os.path.exists(output):
                        os.makedirs(output)
                with open(path, 'w') as f:
                    json.dump(template,f)
                print(Fore.GREEN + f'Temperature_removed sucessfully :{file}...' + Fore.RESET)

    def Missing_module_temp(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
            output = self.output_file + 'Missing_module_removed'
            action_field = 'temperature_difference'
            validator  = ''
        

            for feature in features:
                if feature['properties']['class_name'] != 'missing_module':
                    continue
                else:
                    '''Remove Temperature '''
                    if self.check_feild(feature, file, action_field):
                        temp = feature['properties'][action_field]
                        temp = None
                        feature['properties']['temperature_difference'] = temp
                        validator = 'temp_removed'
                    else:
                        break
                
            if validator == 'temp_removed':
                template = {'type':"FeatureCollection",'name':'pl2','features':features} 
                path = output + '\\' + file + '.json'
                if not os.path.exists(output):
                        os.makedirs(output)
                with open(path, 'w') as f:
                    json.dump(template,f)
                print(Fore.GREEN + f'Missing_module_temperature_removed sucessfully :{file}... ')

            elif validator != 'temp_removed':
                print(Fore.RED + f'No Missing module found : {file}'+ Fore.RESET)

 

    def string_remove(self):
        for file in self.json_dir_list:
            file_path = self.current_dir + "\\" + file
            features = json.load(open(file_path))['features']
            output = self.output_file + 'String_number_removed'
            action_field = 'string_number'
            validator = False


            for feature in features:
                if feature['properties']['class_name'] == 'table' :
                    continue
                else:
                    if self.check_feild(feature, file, action_field):
                        '''Remove Temperature '''
                        string_numbers = feature['properties']['string_number']
                        string_numbers = None
                        feature['properties']['string_number'] =  string_numbers
                        validator = True
                    else:
                        break
            if validator:
                template = {'type':"FeatureCollection",'name':'pl2','features':features} 
                path = output + '\\' + file + '.json'

                if not os.path.exists(output):
                        os.makedirs(output)
                with open(path, 'w') as f:
                    json.dump(template,f)
                print(Fore.GREEN + f'String_number_removed {file}...' + Fore.RESET)





obj = Terminator(current_dir, selected_jsons)

dicto = {'Remove_Module_number': obj.module_number, 'Remove_Temperature':obj.Temp_remove,
          'Remove_Temp/Missing_module': obj.Missing_module_temp, 'Remove_String_numbers':obj.string_remove}

dicto[actions]()






