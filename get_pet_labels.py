#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Michelle
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    # Replace None with the results_dic dictionary that you created with this
    # function
    results_dic = dict()
    filenames = listdir(image_dir)
    filenames_l = listdir(image_dir)
    
    for idx in range(0, len(filenames),1):
        if filenames[idx][0] != ".":
            
            pet_label = ""
            
            filenames[idx] = filenames[idx].lower()
            filenames[idx] = filenames[idx].split("_")
            
            for fileword in filenames[idx] :
                if fileword.isalpha():
                    pet_label += fileword + " "
            pet_label = pet_label.strip()     
           
            if filenames_l[idx] not in results_dic:
                results_dic[filenames_l[idx]] = [pet_label]
            else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
            
                
        
    return results_dic