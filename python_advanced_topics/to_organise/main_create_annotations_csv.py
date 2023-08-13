"""
Project: Fruit size estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021

Description:
    This file creates from a template annotations files for Pychetlabeller.
Use:
    main_create_xml.py
"""
import os

from src.dataset_management.dataset_config import DatasetConfig
from src.dataset_management.dataset_manager import DatasetManager

if __name__ == '__main__':
    """
    Create .csv files for Pychetlabeler tagging. 
    """
    """
    Dataset structure
    
    dataset_root_path \
    | --- \ raw_data
    | --- \ preprocessed_data
        | --- \ dataset_images_path
        | --- \ dataset_annotations_path
        | --- \ dataset_squares_path
    """

    user_path = os.path.join('C:\\', 'Users', 'Usuari')
    base_path = os.path.join(user_path, 'PycharmProjects', 'SizeEstimation', 'test')
    dataset_name = 'KA_Story_RGB_IR_DEPTH_hour---'

    template_filename = 'TEMPLATE_APPLES_ID.csv'
    template_path = os.path.join(base_path, dataset_name, 'preprocessed_data', template_filename)

    dataset_manager_config_obj = DatasetConfig(base_path, dataset_name)
    dataset_manager_obj = DatasetManager(dataset_manager_config_obj)
    dataset_manager_obj.load_template_in_files(template_path)
