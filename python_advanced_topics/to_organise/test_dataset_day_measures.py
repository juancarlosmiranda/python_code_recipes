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
import pandas as pd
import cv2
from src.dataset_management.pascal_voc_parser import PascalVocParser
from src.mass_estimation import DataFeatureProcessor, DataFeatureConfig

from src.dataset_management.dataset_config import DatasetConfig
from src.dataset_management.dataset_manager import DatasetManager


class TestDatasetMeasuresDay(unittest.TestCase):

    def setUp(self):
        self.root_folder = os.path.abspath('.')
        self.dataset_name = 'KA_Story_RGB_IR_DEPTH_dataset'  # HERE WE DEFINE THE NAME OF DATASET, WHATEVER YOU WANT
        self.dataset_root_folder_path = os.path.join(self.root_folder)
        pass

    def test_dataset_day_measures(self):
        BASE_FOLDER = os.path.abspath('.')
        day_measures_filename = 'day_measures.csv'
        path_to_save_df = os.path.join(BASE_FOLDER, 'output_dataset')
        path_day_measures = os.path.join(path_to_save_df, day_measures_filename)

        # create pandas dataframe with columns
        headers_day_measures = ['date_capture', 'time_capture','fruit_id', 'pred.obj_detection', 'pred.measure_c_px',
                                'pred.measure_h_px', 'pred.depth', 'pred.caliber_mm', 'pred.height_mm', 'pred.mass_gr']
        day_measures_df = pd.DataFrame([], columns=headers_day_measures)

        # ---------------------
        dataset_manager_config_obj = DatasetConfig(self.dataset_root_folder_path, self.dataset_name)
        dataset_manager_obj = DatasetManager(dataset_manager_config_obj)
        result_pair_list = dataset_manager_obj.get_labeled_list_files()
        pass

        # data to analyze
        a_rgb_data = None
        a_depth_data = None
        a_ir_data = None

        for a_register in result_pair_list:
            a_date_record = a_register[0]
            a_times_record = a_register[1]
            a_rgb_file_path = a_register[2]
            a_depth_mat_file_path = a_register[3]
            an_ir_mat_file_path = a_register[4]
            a_pv_file_path = a_register[5]

            # select from list image paths previously selected
            # open image and related data
            a_rgb_data = cv2.imread(a_rgb_file_path)  # load data to memory
            a_depth_mat_data = sio.loadmat(a_depth_mat_file_path)  # load data to memory
            a_depth_data = a_depth_mat_data['transformed_depth']
            an_ir_mat_data = sio.loadmat(an_ir_mat_file_path)  # load data to memory
            a_ir_data = an_ir_mat_data['transformed_ir']

            # detections simulated from RGB color images, reading PASCAL VOC files
            # to get bounding boxes and labels
            pv_labelled_list, pv_label_list = PascalVocParser.readXMLFromFile(a_pv_file_path)  # load data to memory

            conf_features = DataFeatureConfig()
            data_feature_processor = DataFeatureProcessor(conf_features, a_rgb_data, a_depth_data)
            results_by_frame_df = data_feature_processor.roi_selector_loop_bbox(pv_labelled_list, pv_label_list)

            # add results by frame to a list
            temporal_record = results_by_frame_df
            temporal_record['fruit_id'] = results_by_frame_df['fruit_id'].astype(str)
            temporal_record['date_capture'] = a_date_record
            temporal_record['time_capture'] = a_times_record

            day_measures_df = day_measures_df.append(temporal_record, ignore_index=True)
            pass
        # -----------------
        day_measures_df.drop(columns=day_measures_df.columns[0], axis=1, inplace=True)
        day_measures_df.to_csv(path_day_measures, float_format='%.2f', sep=';')
        # COMPARATIVE_DF ES USADO PARA LAS METRICAS POR FRAME
        # hay un resultado intermedio que se llama result_by_frame


        # todo: this could be an object structure

        # recover data from folder
        # check that each item has correspondence to an image
        # load data in a list, get a lot of frames to process [OK]
        # with list extract measures from each image [OK]
        # create a datasheet by image analysed [OK]
        # create a summary for the dataset

        # inputs
        # dataset labelled
        # trusted list with pair data
        # configuration of camera
        # final summary name


        # outputs
        # images marked
        # datasheet by each frame
        # datasheet summary
        # datasheet by hour with measures compared to data expert
        # time series of objects along the day

        # ALGORITHM
        # get update list
        # for begin to end of the list
        #   take an element from list
        #   read a frame from dataset
        #   read a depth from dataset
        #   read xml file
        #   convert to array


        """
        output_data/
        | --- \ reports_by_frame
        | --- \ images
        | --- \ reports_by_dataset
        
        """
        # lahora de los archivos

        # get checking with extension
        # get rgb depth
        # get depth
        # check existence of same name with xml extension
        # todo: add to each row the same decimal places after point
        self.assertEqual('OK', 'OK')
        pass

    pass



if __name__ == '__main__':
    unittest.main()
    # configuration objects
    #

# open main dataset
# select data from an specific tree
# read folder, get file name
# read from file name hour data
# call a method to get np_array_by_file(file capture, depth capture, xml mar)
# call a method to process_by_frame(HOUR_CAPTURE, capture_nparray, depth_nparray)
# save measures
# call a method to show on the screen
# call a method to save data
# take measures from detected and labelled data
# add columns from datasheet in one datasheet to compare results.
# calculate measures from data.
# draw data labelled on the screen
# create plots on demand from data.
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
# TODO: corroborar que las manzanas de las figuras se corresponden realmente con el número
# TODO: ver para seleccionar las oclusas y no oclusas
# todo: agregar los parámetros de configuraciones desde las cabeceras.