"""
Project:
Author:
Date:
Description:
...

Use:
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

import os

from src.dataset_management.dataset_config import DatasetConfig
from src.dataset_management.dataset_manager import DatasetManager

if __name__ == '__main__':
    # create dataset flow
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'size_estimation.log')
    path_dataset_config_file = os.path.join(BASE_DIR, 'conf', 'dataset.conf')

    print('Extract videos -->')
    #########################
    # todo: variables for UI
    path_extractor_config_file = os.path.join(BASE_DIR, 'conf', 'frames_extractor.conf')
    # todo: a workhome with a file
    #  process a folder these are variables to input by UI
    an_input_file = os.path.join('C:\\', 'recorded_video', '20210927_114012_k_r2_e_000_150_138.mkv')
    track_file = os.path.join('C:\\', 'exported_images', 'all.txt')
    an_offset = 1  # seconds to start
    a_number_of_frames = 2  # frame
    #########################
    # special config

    # path_images_ouput= C:\Users\Usuari\Downloads\KA_Story_RGB_IR_DEPTH_dataset\preprocessed_data
#    frames_extractor_config_obj = FramesManagerConfig(path_extractor_config_file)
#    frames_extractor_config_obj.path_images_ouput = os.path.join('C:\\', 'Users', 'Usuari', 'Downloads','KA_Story_RGB_IR_DEPTH_dataset', 'preprocessed_data', 'images')
#    track_file = os.path.join('C:\\', 'Users', 'Usuari', 'Downloads','KA_Story_RGB_IR_DEPTH_dataset', 'preprocessed_data', 'images', 'all.txt')
    #########################
    # frames_extractor_config_obj = FramesManagerConfig(path_extractor_config_file)
#    frames_extractor_obj = FramesVideoManager(frames_extractor_config_obj, an_input_file)
#    [frames_written, errors, output_folder] = frames_extractor_obj.export_frames_to_files(track_file, an_offset,
#                                                                                          a_number_of_frames)

    print('Label dataset with external tool -->')

    print('Create dataset')
    ###############################
    # todo: variables for UI
    user_path = os.path.join('C:\\', 'Users', 'Usuari')
    base_path = os.path.join(user_path, 'Downloads')
    dataset_name = 'KA_Story_RGB_IR_DEPTH_dataset'
###############################
    dataset_manager_config_obj = DatasetConfig(base_path, dataset_name)
    dataset_manager_obj = DatasetManager(dataset_manager_config_obj)
    dataset_manager_obj.create_hierarchy()

    print('Load lebeled XML files in dataset')
    ###############################
    #dataset_manager_obj.create_labeled_XML_files()


# todo: make tests for files
# todo: design User interface.
