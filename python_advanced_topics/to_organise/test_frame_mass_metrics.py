"""
Project:
Author:
Date:
Description:
Example taken from https://docs.python.org/3/library/unittest.html
# todo: add header
...

Use: python -m unittest test/test_something.py
"""
import unittest
import os
import scipy.io as sio
import cv2
import time
from src.dataset_management.pascal_voc_parser import PascalVocParser
from src.mass_estimation import DataFeatureProcessor, DataFeatureConfig


class TestFramesMassMetrics(unittest.TestCase):

    def setUp(cls):
        print("setUpClass(cls) -->")

    def test_frame_metrics(self):
        print(type(self).__name__, '--> test_frame_metrics(self) -->')
        root_folder = os.path.abspath('.')
        # dataset definition
        rgb_file_name_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_C.png'
        depth_file_name_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_D.mat'
        ir_file_name_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_I.mat'
        file_pv_to_check = 'TREE_02.xml'

        dataset_name = 'KA_Story_RGB_IR_DEPTH_dataset'  # HERE WE DEFINE THE NAME OF DATASET
        dataset_folder_path = os.path.join(root_folder, dataset_name, 'preprocessed_data')
        dataset_folder_img_path = os.path.join(dataset_folder_path, 'images')
        dataset_folder_pv_path = os.path.join(dataset_folder_path, 'square_annotations1')

        # path to files for test
        a_rgb_file_path = os.path.join(dataset_folder_img_path, rgb_file_name_to_check)
        a_depth_mat_file_path = os.path.join(dataset_folder_img_path, depth_file_name_to_check)
        an_ir_mat_file_path = os.path.join(dataset_folder_img_path, ir_file_name_to_check)
        a_pv_file_path = os.path.join(dataset_folder_pv_path, file_pv_to_check)

        # data to analyze
        a_rgb_data = None
        a_depth_data = None
        a_ir_data = None

        a_rgb_data = cv2.imread(a_rgb_file_path)  # load data to memory
        a_depth_mat_data = sio.loadmat(a_depth_mat_file_path)  # load data to memory
        a_depth_data = a_depth_mat_data['transformed_depth']
        # TODO: DON´T DELETE IT!!!!
        an_ir_mat_data = sio.loadmat(an_ir_mat_file_path)  # load data to memory
        a_ir_data = an_ir_mat_data['transformed_ir']

        # detections simulated from RGB color images, reading PASCAL VOC files
        # to get bounding boxes and labels
        pv_labelled_list, pv_label_list = PascalVocParser.readXMLFromFile(a_pv_file_path)  # load data to memory
        # --------------------------------
        # from here detection pipeline
        # --------------------------------
        # input, color image and depth image, return list of object detected and measures
        # todo: el detector sabe si los objetos enviados corresponden al criterio de filtro
        #  por coordenadas
        # need a filtered objects, to save time

        conf_features = DataFeatureConfig()
        image_name = 'a_processed_image'
        data_feature_processor = DataFeatureProcessor(conf_features, a_rgb_data, a_depth_data)
        label_filter = None  # todo: check if this is necessary
        # ----------------------------------------
        time_1 = time.time()  # BEGIN TIME CONTROL
        table_by_frame = data_feature_processor.roi_selector_loop_bbox(pv_labelled_list, pv_label_list)
        # ----------------------------------------
        time_2 = time.time()  # END TIME CONTROL
        time_total = time_2 - time_1
        print('time_total',time_total)
        table_all_detections = []
        # --------------------------------
        # write data table by frame each detection and measures
        BASE_FOLDER = os.path.abspath('.')
        df_file_name = 'measures_by_frame.csv'
        path_to_save_df = os.path.join(BASE_FOLDER, df_file_name)

        headers_resume_frame = ['pred.obj_detection', 'fruit_id', 'pred.measure_c_px', 'pred.measure_h_px',
                                'pred.depth', 'pred.caliber_mm',
                                'pred.height_mm',
                                'pred.mass_gr']

        table_by_frame.to_csv(path_to_save_df, float_format='%.2f', sep=';')
        total_frame_objects = table_by_frame['pred.mass_gr'].count()
        total_frame_yield = table_by_frame['pred.mass_gr'].sum()
        print(f'total_frame_objects-> {total_frame_objects}')
        print(f'total_frame_yield-> {total_frame_yield/1000} kg')
        # put here total count of objects and total data in kg
        self.assertEqual('OK', 'OK')


if __name__ == '__main__':
    unittest.main()



