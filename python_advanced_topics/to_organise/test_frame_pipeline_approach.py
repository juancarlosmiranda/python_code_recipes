"""
Project:
Author:
Date:
Description:
Example taken from https://docs.python.org/3/library/unittest.html

...

Use: python -m unittest tests/test_something.py
"""
import unittest
import os
import numpy as np
import scipy.io as sio
import scipy.stats as stats
import cv2
import time
from src.dataset_management.pascal_voc_parser import PascalVocParser
from src.mass_estimation import SizeEstimation, CameraParameters
from src.mass_estimation import MassEstimation, MassEstimationModelSelector


class TestFramesPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass(cls) -->")

    def test_process_pipeline_frame(self):
        print(type(self).__name__, '--> test_process_pipeline_frame(self): -->')
        root_folder = os.path.abspath('.')
        # dataset definition
        rgb_file_name_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_C.png'
        depth_file_name_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_D.mat'
        ir_file_name_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_I.mat'
        file_pv_to_check = '20210927_115932_k_r2_e_000_150_138_1_0_C.xml'

        dataset_name = 'KA_Story_RGB_IR_DEPTH_dataset'  # HERE WE DEFINE THE NAME OF DATASET
        dataset_folder_path = os.path.join(root_folder, dataset_name, 'preprocessed_data')
        dataset_folder_img_path = os.path.join(dataset_folder_path, 'images')
        dataset_folder_pv_path = os.path.join(dataset_folder_path, 'square_annotations1')

        # path to files for test
        a_rgb_file_path = os.path.join(dataset_folder_img_path, rgb_file_name_to_check)
        a_depth_mat_file_path = os.path.join(dataset_folder_img_path, depth_file_name_to_check)
        an_ir_mat_file_path = os.path.join(dataset_folder_img_path, ir_file_name_to_check)
        a_pv_file_path = os.path.join(dataset_folder_pv_path, file_pv_to_check)

        pv_labelled_list, pv_label_list = PascalVocParser.readXMLFromFile(a_pv_file_path)  # load data to memory

        # data to analyze
        a_rgb_data = None
        a_depth_data = None
        a_ir_data = None

        a_rgb_data = cv2.imread(a_rgb_file_path)  # load data to memory
        a_depth_mat_data = sio.loadmat(a_depth_mat_file_path)  # load data to memory
        a_depth_data = a_depth_mat_data['transformed_depth']
        # todo: NO BORRAR!!!!
        an_ir_mat_data = sio.loadmat(an_ir_mat_file_path)  # load data to memory
        a_ir_data = an_ir_mat_data['transformed_ir']


        # to crop images
        #human_labeled_MATLAB_list = [
        #    [1299, 363, 91, 91],
        #    [1236, 354, 44, 43],
        #]

        # --------------------------
        # in PASCAL VOC format list
        #human_labeled_list = [
        #    [1299, 363, 1390, 454],
        #    [1236, 354, 1280, 397],
        #]
        # --------------------------

        n = 22  #5) apple 02124 80,7 71,01 217,7 gr
        xmin = int(pv_labelled_list[n][0])
        ymin = int(pv_labelled_list[n][1])
        xmax = int(pv_labelled_list[n][2])
        ymax = int(pv_labelled_list[n][3])

        if ymin == 0:
            ymin = 1

        if xmin == 0:
            xmin = 1

        time_1 = time.time()  # BEGIN TIME CONTROL

        a_rgb_cropped = a_rgb_data[ymin:ymax, xmin:xmax]
        a_depth_cropped = a_depth_data[ymin:ymax, xmin:xmax]
        #a_ir_cropped = a_ir_data[ymin:ymax, xmin:xmax]

        #cv2.imshow('rgb', a_rgb_data)
        #cv2.imshow('depth', colorize(a_depth_data, (None, 5000)))
        #cv2.imshow('ir', colorize(a_ir_data, (None, 5000)))
        #cv2.imshow('cropped', a_rgb_cropped)
        #cv2.imshow('depth cropped', colorize(a_depth_cropped, (None, 5000)))
        #cv2.imshow('ir cropped', colorize(a_ir_cropped, (None, 5000)))

        #cv2.waitKey()
        #cv2.destroyAllWindows()

        # get statistics measures depth statistics
        temporalDepthFilter = a_depth_cropped > 0
        temporalDepthSelected = a_depth_cropped[temporalDepthFilter]  # to get statistics descriptive

        meanDepth = np.mean(temporalDepthSelected)
        stdDepth = np.std(temporalDepthSelected)
        minDepth = np.min(temporalDepthSelected)
        maxDepth = np.max(temporalDepthSelected)
        modeDepth = stats.mode(temporalDepthSelected, axis=None)[0][0]

        current_label = pv_label_list[n]
        print(f'{n}) MDepth={meanDepth} stdDepth={stdDepth} minDepth={minDepth} maxDepth={maxDepth} modeDepth={modeDepth} {current_label}')

        # ----------------------------------------
        measure_c_px = xmax - xmin
        measure_h_px = ymax - ymin
        depth_measured_mm = modeDepth # todo: change this
        camera_conf = CameraParameters()
        obj_size_estimation = SizeEstimation(camera_conf)
        result_estimation_c_mm = obj_size_estimation.estimate_size(depth_measured_mm, measure_c_px)
        result_estimation_h_mm = obj_size_estimation.estimate_size(depth_measured_mm, measure_h_px)
        correction_value=1  # todo: check this coefficient
        fix_estimation_c_mm = correction_value * result_estimation_c_mm
        fix_estimation_h_mm = correction_value * result_estimation_h_mm

        # ----------------------------------------
        a_caliber_mm = fix_estimation_c_mm
        an_height_mm = fix_estimation_h_mm
        # mass estimation by size in millimeter
        obj_mass_estimation = MassEstimation()
        result_mass_estimation = obj_mass_estimation.predict_weight(a_caliber_mm, an_height_mm, weight_method_selector=MassEstimationModelSelector.CH_LM_MET_01)

        print('current_label -->', current_label)
        print('depth_measured_mm -->', depth_measured_mm)
        print('measure_c_px -->', measure_c_px)
        print('measure_h_px -->', measure_h_px)
        print('result_estimation_c_mm -->', correction_value*result_estimation_c_mm)
        print('result_estimation_h_mm -->', correction_value*result_estimation_h_mm)
        print(f'result__mass_estimation {result_mass_estimation} gr->')

        print(f'{n}) current_label={current_label} measure_c_px={measure_c_px} measure_h_px={measure_h_px} fix_estimation_c_mm={fix_estimation_c_mm} fix_estimation_h_mm={fix_estimation_h_mm} result_mass_estimation={result_mass_estimation} gr')

        # ----------------------------------------
        time_2 = time.time()  # END TIME CONTROL
        time_total = time_2 - time_1
        print('time_total',time_total)



        pass

        self.assertEqual('OK', 'OK')


if __name__ == '__main__':
    unittest.main()

    # create experimental dataset with Pychetlabeller [OK]
    # extract one frame [OK]
    # load rgb color [OK]
    # load matrix data [OK]
    # get coordinates of bounding boxes as an array list. [OK]
    # get depth from every region marked [OK]
    # calculate size with depth [OK]
    # calculate size in milimeters with depth [OK]
    # with milimeters estimate mass of each object [OK]
    # save results in a list by each frame.
    # add every result from frame to overall count
    # DIBUJAR LOS RECUADROS CON LA ETIQYETA, EL TAMAÑO Y LA MASA EN GR

    # evaluar si los recortes python son iguales a MATLAB
    # evaluar si calcula igual las medidas de tendencia central en Python
    # Hacer la clase que migra PASCAL VOC.
    # Hacer la clase que calcula los tamaños.
    # Unir para el recorrido de un frame. Ver como hacer para que en menos ciclos detecte los parámetros
    # Armar una hoja de cálculo
    # refactor this project to include tests files in every folder.
    # Falta un detector de la zona donde se juntan las cámaras, tal que se pueda contabilizar alli.
    # Arreglar MATLAB para coordinar el trabajo en conjunto y que tengan los mismos nombres de clases


