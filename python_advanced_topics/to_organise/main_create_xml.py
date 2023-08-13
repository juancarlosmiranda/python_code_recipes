"""
Project: Fruit size estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021

Description:
    This file migrates objects labelled with Pychetlabeller to .xml format.
Use:
    main_create_xml.py
"""
import os

from src.dataset_management.dataset_config import DatasetConfig
from src.dataset_management.dataset_manager import DatasetManager

if __name__ == '__main__':
    """
    Create .xml files from files generated in Pychetlabeler tagging. 
    """
    # user_path = os.path.join('C:\\', 'Users', 'Usuari')
    # base_path = os.path.join(user_path, 'Downloads')
    # dataset_root_folder = os.path.join('KA_Story_RGB_IR_DEPTH_dataset', 'preprocessed_data')

    # images_sub_folder = 'images'
    # annotations_sub_folder = 'annotations'
    # squares_sub_folder = 'square_annotations1'
    # img_extension = '.png'
    # csv_extension = '.csv'
    # xml_extension = '.xml'

    # class_label_name = "APPLE"

    """
    Dataset structure
    
    dataset_root_path \
    | --- \ raw_data
    | --- \ preprocessed_data
        | --- \ dataset_images_path
        | --- \ dataset_annotations_path
        | --- \ dataset_squares_path
    """

    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'size_estimation.log')
    path_dataset_config_file = os.path.join(BASE_DIR, 'conf', 'dataset.conf')

    # input parameters
    # an_input_file = os.path.join('C:\\','recorded_video','20210927_114012_k_r2_e_000_150_138.mkv')

    #

    # user_path = os.path.join('C:\\', 'Users', 'Usuari')
    # base_path = os.path.join(user_path, 'Downloads')
    # dataset_name = 'KA_Story_RGB_IR_DEPTH_dataset'

    user_path = os.path.join('C:\\', 'Users', 'Usuari')
    base_path = os.path.join(user_path, 'PycharmProjects', 'SizeEstimation', 'test')
    dataset_name = 'KA_Story_RGB_IR_DEPTH_hour_5f_mask'

    label_filename = 'labelmap_apples_id.json'
    label_json_path = os.path.join(base_path, dataset_name, 'preprocessed_data', label_filename)



    dataset_manager_config_obj = DatasetConfig(base_path, dataset_name)
    dataset_manager_obj = DatasetManager(dataset_manager_config_obj)
    dataset_manager_obj.create_XML_files(label_json_path)

