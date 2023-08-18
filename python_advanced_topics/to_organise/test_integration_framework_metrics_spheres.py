"""
Project: Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: February 2022
Description:
    File to test each step in data extraction

Use:
    python -m unittest test/test_integration_framework_metrics.py
"""

import unittest
import os
import pandas as pd
# ------------------
from datetime import datetime
from src.dataset_management.dataset_config import DatasetConfig
# ------------------
from src.mass_estimation import AzureKinect
from src.mass_estimation import DataFeatureConfig
from src.mass_estimation import DepthSelector
from src.mass_estimation import ComparativeMeasuresReportSelector
from src.reports_management.prediction_metrics_framework import PredictionsMetricsFrameworkConfig
from src.reports_management.prediction_metrics_framework import PredictionMetricsFramework
# ------------------


class TestMassEstimationMetricsFramework(unittest.TestCase):

    def setUp(self):
        self.root_folder = os.path.abspath('../')
        self.dataset_name = 'KA_Story_RGB_IR_DEPTH_hour_5f'  # HERE WE DEFINE THE NAME OF DATASET, WHATEVER YOU WANT
        self.dataset_root_folder_path = os.path.join(self.root_folder)
        self.path_input_csv = os.path.join(self.root_folder, 'input_dataset')
        self.path_output_simulation = os.path.join(self.root_folder, 'output_dataset')
        self.path_output_plots = os.path.join(self.path_output_simulation, 'plots')

        now = datetime.now()
        self.datetime_experiment = now.strftime("%Y%m%d_%H%M%S_")
        self.day_measures_filename = self.datetime_experiment+'comparative_by_day_B.csv'
        self.path_output_csv = os.path.join(self.path_output_simulation, 'output_csv')
        self.path_day_measures = os.path.join(self.path_output_csv, self.day_measures_filename)

        # --------------------------------------
        # LABORATORY MEASURES
        # --------------------------------------
        tree_selector = '2'
        lab_input_filename = 'CALIBRATION_SPHERES_v1.csv'  # HERE WE DEFINE THE NAME OF MANUAL MEASURES
        path_input_dataset = os.path.join(self.root_folder, 'csv_datasets')
        path_manual_measures_df = os.path.join(path_input_dataset, lab_input_filename)
        manual_measures_df = pd.read_csv(path_manual_measures_df, dtype=str, sep=';')
        manual_measures_df['fruit_id'] = manual_measures_df['fruit_id'].astype(str)
        manual_measures_df['lab.caliber_mm'] = manual_measures_df['lab.caliber_mm'].astype(float)
        manual_measures_df['lab.height_mm'] = manual_measures_df['lab.height_mm'].astype(float)
        manual_measures_df['lab.weight_gr'] = manual_measures_df['lab.weight_gr'].astype(float)
        self.measures_selected_df = manual_measures_df
        # --------------------------------------
        dataset_manager_config = DatasetConfig(self.dataset_root_folder_path, self.dataset_name)
        # todo: check dataset hierarchy, add controls to this
        # todo: put libraries to convert data from bounding boxes, or masks
        camera_option = AzureKinect()
        depth_option = DepthSelector.AVG
        mass_estimation_option = None  #MassEstimationModelSelector.CUBIC_LINEAR_C
        data_features_options = DataFeatureConfig(camera_conf=camera_option.rgb_sensor,
                                                depth_selector=depth_option,
                                                mass_selector=mass_estimation_option)

        comparative_report_option = ComparativeMeasuresReportSelector.A1
        self.simulator_config = PredictionsMetricsFrameworkConfig(dataset_manager_config, self.path_day_measures, data_features_options, mass_estimation_option, comparative_report_option)



    def test_run_simulation(self):
        simulator_metrics = PredictionMetricsFramework(self.simulator_config)
        simulator_metrics.comparative_metrics_dataset_bbox(self.measures_selected_df)
        results_simulation_metrics = simulator_metrics.get_simulation_results()
        results_simulation_metrics.print_metrics()
        simulator_metrics.export_csv_results(self.path_day_measures)

        # todo: run simulation in verbose mode, showing time execution of process
        # TODO: LABORATORY_MEASURES MUST HAVE A SELECTED DATA as previous requisites
        # todo: run_comparative_dataset_metrics(_LABORATORY_MEASURES)
        # todo: run_comparative_frame_metrics(A_NAME_FOR_A_FRAME)
        # todo: get_comparative_metrics() RMSE, MSE, MAPE

        # todo: run_calculate_measures_frame()
        # todo: run_calculate_measures_dataset()
        # todo: this could be an object structure

        """
        output_data/
        | --- \ reports_by_frame
        | --- \ images
        | --- \ reports_by_dataset
        
        """
        self.assertEqual('OK', 'OK')



if __name__ == '__main__':
    unittest.main()