import time
import os
import shutil

path = input("Please Enter the Path : ")
days = 30
seconds = time.time()-(days*24*60*60)
deletd_folder_count = 0
deletd_file_count = 0

if os.path.exists(path):
    for root_folder,folders,files in os.walk(path):
        if seconds>=get_file_or_folder_age(root_folder):
            remove_folder(root_folder)
            deletd_folder_count+= 1
            break
        else :
            for folder in folders:
                folder_path = os.path.join(root_folder,folder)
                if seconds>=get_file_or_folder_age(folder_path):
                         remove_folder(folder_path)
                         deletd_folder_count+= 1

            for file in files:
                file_path = os.path.join(root_folder,file)
                if seconds>=get_file_or_folder_age(file_path):
                         remove_folder(file_path)
                         deletd_file_count+= 1
                

                
                     
        

