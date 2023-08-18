"""
Project:
Author:
Date:
Description:
Example taken from https://docs.python.org/3/library/unittest.html
# todo: add header
# todo: add from test new reports
...

Use: python -m unittest test/test_something.py
"""
import unittest
import os
import scipy.io as sio
import pandas as pd
import cv2
import time
import math
from src.dataset_management.pascal_voc_parser import PascalVocParser
from src.mass_estimation import DataFeatureProcessor, DataFeatureConfig
from sklearn.metrics import mean_squared_error, median_absolute_error, mean_absolute_percentage_error, r2_score


class TestFrameComparativeMeasures(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUpClass(cls) -->")

    def test_frame_measures(self):
        print(type(self).__name__, '--> test_frame_measures(self): -->')
        root_folder = os.path.abspath('.')
        # dataset definition
        rgb_file_name_to_check = '20210927_114012_k_r2_e_000_150_138_2_0_C.png'
        depth_file_name_to_check = '20210927_114012_k_r2_e_000_150_138_2_0_D.mat'
        ir_file_name_to_check = '20210927_114012_k_r2_e_000_150_138_2_0_I.mat'
        file_pv_to_check = '20210927_114012_k_r2_e_000_150_138_2_0_C.xml'

        dataset_name = 'KA_Story_RGB_IR_DEPTH_hour_5f'  # HERE WE DEFINE THE NAME OF DATASET
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
        data_feature_processor = DataFeatureProcessor(conf_features, a_rgb_data, a_depth_data)
        # ----------------------------------------
        time_1 = time.time()  # BEGIN TIME CONTROL
        results_by_frame_df = data_feature_processor.roi_selector_loop_bbox(pv_labelled_list, pv_label_list)
        # ----------------------------------------
        time_2 = time.time()  # END TIME CONTROL
        time_total = time_2 - time_1
        print('time_total', time_total)
        table_all_detections = []
        # --------------------------------
        # write data table by frame each detection and measures
        # --------------------------------
        BASE_FOLDER = os.path.abspath('.')
        by_filename = 'results_by_frame.csv'
        comparative_filename = 'comparative_by_frame.csv'
        path_to_save_df = os.path.join(BASE_FOLDER, 'output_dataset')
        path_results_measured_df = os.path.join(path_to_save_df, by_filename)  # todo: put data
        path_comparative = os.path.join(path_to_save_df, comparative_filename)  # todo: put data

        # files to use, import data from manual measures
        path_input_dataset = os.path.join(BASE_FOLDER, 'csv_datasets')
        lab_input_filename = 'fruit_measures_ALL_TREES_01-12_comma_id_v1.csv'
        path_input_dataset_df = os.path.join(path_input_dataset, lab_input_filename)  # todo: put data
        manual_measures_df = pd.read_csv(path_input_dataset_df, dtype=str, sep=';')
        manual_measures_df['fruit_id'] = manual_measures_df['fruit_id'].astype(str)
        manual_measures_df['lab.caliber_mm'] = manual_measures_df['lab.caliber_mm'].astype(float)  # todo: check decimals
        manual_measures_df['lab.height_mm'] = manual_measures_df['lab.height_mm'].astype(float)
        manual_measures_df['lab.weight_gr'] = manual_measures_df['lab.weight_gr'].astype(float)
        tree_selected_df = manual_measures_df[manual_measures_df["lab.tree"] == '2']  # todo: add parameter configuration
        results_by_frame_df.to_csv(path_results_measured_df, float_format='%.2f', sep=';')

        # ancillary calculation
        comparative_df = pd.merge(tree_selected_df, results_by_frame_df, left_on='fruit_id', right_on='fruit_id', how='inner')
        total_objects = comparative_df.shape[0]  # todo change this to another field

        # ADDING NEW COLUMNS TO REPORT
        # ---------------
        # caliber
        # ---------------
        comparative_df['caliber_abs_dif'] = abs(comparative_df['pred.caliber_mm'] - comparative_df['lab.caliber_mm'])  # todo: predicted - measured in lab
        comparative_df['caliber_mape_abs_dif'] = abs((comparative_df['lab.caliber_mm']-comparative_df['pred.caliber_mm'])/comparative_df['lab.caliber_mm'])  # todo: measured in lab - predicted
        comparative_df['caliber_sqr_dif'] = pow((comparative_df['pred.caliber_mm'] - comparative_df['lab.caliber_mm']),2)
        mean_lab_caliber = comparative_df['lab.caliber_mm'].mean()  # todo: check this decimals could be cause of errors!!
        comparative_df['caliber_sqr_mean_dif'] = pow((comparative_df['lab.caliber_mm'] - mean_lab_caliber),2)  # todo: this has errors
        total_sqr_dif_caliber = comparative_df['caliber_sqr_dif'].sum()
        total_abs_dif_caliber = comparative_df['caliber_abs_dif'].sum()
        total_mape_abs_dif_caliber = comparative_df['caliber_mape_abs_dif'].sum()
        total_r1 = total_sqr_dif_caliber
        total_r2 = comparative_df['caliber_sqr_mean_dif'].sum()


        MSE_caliber = total_sqr_dif_caliber/total_objects
        MAE_caliber = total_abs_dif_caliber/total_objects
        RMSE_caliber = math.sqrt(total_sqr_dif_caliber/total_objects)
        MAPE_caliber = total_mape_abs_dif_caliber/total_objects
        R2_caliber = 1 - (total_r1/total_r2)


        print('--- CALIBER MEASURES ---')
        print(f'total_objects-> {total_objects}')
        print(f'mean_lab_caliber ={mean_lab_caliber}')
        print(f'RMSE_caliber ={RMSE_caliber}')
        print(f'MSE_caliber ={MSE_caliber}')
        print(f'MAE_caliber ={MAE_caliber} mm.')
        print(f'MAPE_caliber ={MAPE_caliber} %')
        print(f'R2_caliber={R2_caliber}')

        y_true = comparative_df['lab.caliber_mm']
        y_pred = comparative_df['pred.caliber_mm']

        mse_caliber = mean_squared_error(y_true, y_pred)
        mae_caliber = median_absolute_error(y_true, y_pred)
        mape_caliber = mean_absolute_percentage_error(y_true, y_pred)
        r2_caliber = r2_score(y_true, y_pred)

        print(f'mse_caliber={mse_caliber}')
        print(f'mae_caliber={mae_caliber} mm.')
        print(f'mape_caliber={mape_caliber} %')
        print(f'r2_caliber={r2_caliber}')


        # ---------------
        # height
        # ---------------
        comparative_df['height_abs_dif'] = abs(comparative_df['pred.height_mm'] - comparative_df['lab.height_mm'])  # todo: predicted - measured in lab
        comparative_df['height_mape_abs_dif'] = abs((comparative_df['lab.height_mm']-comparative_df['pred.height_mm'])/comparative_df['lab.height_mm'])  # todo: measured in lab - predicted
        comparative_df['height_sqr_dif'] = pow((comparative_df['pred.height_mm'] - comparative_df['lab.height_mm']),2)
        mean_lab_height = comparative_df['lab.height_mm'].mean()  # todo: check this decimals could be cause of errors!!
        comparative_df['height_sqr_mean_dif'] = pow((comparative_df['lab.height_mm'] - mean_lab_height),2)  # todo: this has errors
        total_sqr_dif_height = comparative_df['height_sqr_dif'].sum()
        total_abs_dif_height = comparative_df['height_abs_dif'].sum()
        total_mape_abs_dif_height = comparative_df['height_mape_abs_dif'].sum()
        total_r1 = total_sqr_dif_height
        total_r2 = comparative_df['height_sqr_mean_dif'].sum()


        MSE_height = total_sqr_dif_height/total_objects
        MAE_height = total_abs_dif_height/total_objects
        RMSE_height = math.sqrt(total_sqr_dif_height/total_objects)
        MAPE_height = total_mape_abs_dif_height/total_objects
        R2_height = 1 - (total_r1/total_r2)


        print('--- HEIGHT MEASURES ---')
        print(f'total_objects-> {total_objects}')
        print(f'mean_lab_height ={mean_lab_height}')
        print(f'RMSE_height ={RMSE_height}')
        print(f'MSE_height ={MSE_height}')
        print(f'MAE_height ={MAE_height} mm.')
        print(f'MAPE_height ={MAPE_height} %')
        print(f'R2_height={R2_height}')

        y_true = comparative_df['lab.height_mm']
        y_pred = comparative_df['pred.height_mm']

        mse_height = mean_squared_error(y_true, y_pred)
        mae_height = median_absolute_error(y_true, y_pred)
        mape_height = mean_absolute_percentage_error(y_true, y_pred)
        r2_height = r2_score(y_true, y_pred)

        print(f'mse_height={mse_height}')
        print(f'mae_height={mae_height} mm.')
        print(f'mape_height={mape_height} %')
        print(f'r2_height={r2_height}')



        # ---------------
        # WEIGHT
        # ---------------
        comparative_df['weight_abs_dif'] = abs(comparative_df['pred.mass_gr'] - comparative_df['lab.weight_gr'])  # todo: predicted - measured in lab
        comparative_df['weight_mape_abs_dif'] = abs((comparative_df['lab.weight_gr']-comparative_df['pred.mass_gr'])/comparative_df['lab.weight_gr'])  # todo: measured in lab - predicted
        comparative_df['weight_sqr_dif'] = pow((comparative_df['pred.mass_gr'] - comparative_df['lab.weight_gr']),2)
        mean_lab_weight = comparative_df['lab.weight_gr'].mean()  # todo: check this decimals could be cause of errors!!
        comparative_df['weight_sqr_mean_dif'] = pow((comparative_df['lab.weight_gr'] - mean_lab_weight),2)  # todo: this has errors

        total_lab_yield = comparative_df['lab.weight_gr'].sum()
        total_frame_yield = comparative_df['pred.mass_gr'].sum()
        total_sqr_dif_weight = comparative_df['weight_sqr_dif'].sum()
        total_abs_dif_weight = comparative_df['weight_abs_dif'].sum()
        total_mape_abs_dif_weight = comparative_df['weight_mape_abs_dif'].sum()
        total_r1 = total_sqr_dif_weight
        total_r2 = comparative_df['weight_sqr_mean_dif'].sum()

        MSE_weight = total_sqr_dif_weight/total_objects
        MAE_weight = total_abs_dif_weight/total_objects
        RMSE_weight = math.sqrt(total_sqr_dif_weight/total_objects)
        MAPE_weight = total_mape_abs_dif_weight/total_objects
        R2_weight = 1 - (total_r1/total_r2)

        print('--- WEIGHT MEASURES ---')
        print(f'total_objects-> {total_objects}')
        print(f'total_lab_yield-> {total_lab_yield} gr, {total_lab_yield/1000} kg')
        print(f'total_frame_yield-> {total_frame_yield} gr, {total_frame_yield/1000} kg')
        print(f'mean_lab_weight-> {mean_lab_weight} gr, {mean_lab_weight/1000} kg')
        print(f'RMSE_weight ={RMSE_weight}')
        print(f'MSE_weight ={MSE_weight}')
        print(f'MAE_weight ={MAE_weight} gr.')
        print(f'MAPE_weight ={MAPE_weight} %')
        print(f'R2_weight={R2_weight}')

        # ------------------------
        # using sklearn library
        # ------------------------
        y_true = comparative_df['lab.weight_gr']
        y_pred = comparative_df['pred.mass_gr']
        mse_weight = mean_squared_error(y_true, y_pred)
        mae_weight = median_absolute_error(y_true, y_pred)
        mape_weight = mean_absolute_percentage_error(y_true, y_pred)
        r2_weight = r2_score(y_true, y_pred)
        print(f'mse_weight={mse_weight}')
        print(f'mae_weight={mae_weight} gr.')
        print(f'mape_weight={mape_weight} %')
        print(f'r2_weight={r2_weight}')

        # put here total count of objects and total data in kg

        # save dataframe
        comparative_df.to_csv(path_comparative, float_format='%.2f', sep=';')

        pass
        # todo: add to each row the same decimal places after point
        self.assertEqual('OK', 'OK')


if __name__ == '__main__':
    unittest.main()

# open main dataset
# select data from an specific tree
# take measures from detected and labelled data
# add columns from datasheet in one datasheet to compare results.
# calculate measures from data.
# draw data labelled on the screen
# label data and create a dataset to test scripts

# todo: hacer el test para las cabeceras de los archivos, de manera a saber si estos cambian.
# todo: agregar las metricas para saber si calculan bien los datos de las tablas
# todo: agregar los parámetros externos.
# todo: agregar el ciclo pàra que lea imagenes etiquetadas y obtenga metricas.
# todo: agregar graficos para ver la correlacion de variables
# todo: agregar como parámetros el metodo para obtener la regresion.
# ------------
# DONE
# ------------
# todo: agregar profundidad a las columnas [OK]
# todo: check equations [OK]
# todo: add calculation [OK]
# todo: add header tests, it is necessary to check tablas headers [OK]

# ANTES DE LOS TEST DE EXACTITUD
# TODO: CONFIGURAR LOS PARAMETROS DE LA AZURE
# TODO: ELEGIR MANZANAS QUE ESTÁN EN EL PUNTO DE SOLAPAMIENTO DE LOS SENSORES DE PROFUNDIDAD Y COLOR
# TODO: corroborar que las manzanas de las figuras se corresponden realmente con el númeor

# todo: obtener los valores para graficas por frame para hacer rápido los gráficos.
