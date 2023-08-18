"""
Project: Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: February 2022
Description:
    File to extract results in a datasheet
    It is a test suite of several parameters config
    Works with all possible combinations of methods and measures calibration spheres

Use:
    python -m unittest test/test_integration_framework_datasheet_spheres.py
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
from src.mass_estimation import ROISelector
from src.mass_estimation import SizeEstimationSelector
from src.mass_estimation import DepthSelector
from src.mass_estimation import MassEstimationModelSelector
from src.mass_estimation import ComparativeMeasuresReportSelector
from src.reports_management.prediction_metrics_framework import PredictionsMetricsFrameworkConfig
from src.reports_management.prediction_metrics_framework import PredictionMetricsFramework
# ------------------


class TestIntegrationDatasheetSpheres(unittest.TestCase):

    def setUp(self):
        self.root_folder = os.path.abspath('../')
        self.dataset_name = 'KA_Story_RGB_IR_DEPTH_hour_5f'  # HERE WE DEFINE THE NAME OF DATASET, WHATEVER YOU WANT
        self.dataset_root_folder_path = os.path.join(self.root_folder)
        self.path_input_csv = os.path.join(self.root_folder, 'input_dataset')
        self.path_output_simulation = os.path.join(self.root_folder, 'output_dataset')
        self.path_output_plots = os.path.join(self.path_output_simulation, 'plots')

        now = datetime.now()
        self.datetime_experiment = now.strftime("%Y%m%d_%H%M%S_")
        self.day_measures_filename = self.datetime_experiment + 'comparative_by_day.csv'
        self.path_output_csv = os.path.join(self.path_output_simulation, 'output_csv')
        self.path_day_measures = os.path.join(self.path_output_csv, self.day_measures_filename)
        # --------------
        # create optimization datasheet
        self.headers_optimization = ['camera_option', 'pixel_option', 'size_estimation_option', 'depth_option', 'mass_estimation_option',
                                     'comparative_report_option', 'total_objects', 'unit_of_measurement', 'MSE', 'MAE',
                                     'RMSE', 'MAPE', 'R2']
        self.optimization_filename = self.datetime_experiment + 'optimization_results_spheres.csv'
        self.path_optimization = os.path.join(self.path_output_csv, self.optimization_filename)
        self.optimization_results_df = pd.DataFrame([], columns=self.headers_optimization)
        # --------------------------------------
        # LABORATORY MEASURES
        # --------------------------------------
        tree_selector = '2'
        lab_input_filename = 'CALIBRATION_SPHERES_v1.csv' # HERE WE DEFINE THE NAME OF MANUAL MEASURES
        path_input_dataset = os.path.join(self.root_folder, 'csv_datasets')
        path_manual_measures_df = os.path.join(path_input_dataset, lab_input_filename)
        manual_measures_df = pd.read_csv(path_manual_measures_df, dtype=str, sep=';')
        manual_measures_df['fruit_id'] = manual_measures_df['fruit_id'].astype(str)
        manual_measures_df['lab.caliber_mm'] = manual_measures_df['lab.caliber_mm'].astype(
            float)  # todo: check decimals
        manual_measures_df['lab.height_mm'] = manual_measures_df['lab.height_mm'].astype(float)
        manual_measures_df['lab.weight_gr'] = manual_measures_df['lab.weight_gr'].astype(float)
        #self.measures_selected_df = manual_measures_df[manual_measures_df["lab.tree"] == tree_selector]  # todo: add parameter configuration

        self.measures_selected_df = manual_measures_df
        # --------------------------------------
        self.dataset_manager_config = DatasetConfig(self.dataset_root_folder_path, self.dataset_name)
        # todo: check dataset hierarchy, add controls to this
        # todo: save in file
        # todo: put libraries to convert data from bounding boxes, or masks
        self.camera_option = AzureKinect()
        self.depth_option = DepthSelector.AVG
        self.mass_estimation_option = None  #MassEstimationModelSelector.MULTIPLE_LINEAR_C_H
        self.data_features_options = DataFeatureConfig(camera_conf=self.camera_option.rgb_sensor,
                                                       depth_selector=self.depth_option,
                                                       mass_selector=self.mass_estimation_option)

        self.comparative_report_option = ComparativeMeasuresReportSelector.A1
        self.simulator_config = PredictionsMetricsFrameworkConfig(self.dataset_manager_config,
                                                                  self.path_day_measures, self.data_features_options,
                                                                  self.mass_estimation_option,
                                                                  self.comparative_report_option)

    def bbox_simulation_method_1(self):
        self.roi_selector = ROISelector.BBOX
        self.size_estimation_selector = SizeEstimationSelector.BBOX
        self.depth_option = DepthSelector.AVG
        self.mass_estimation_option = MassEstimationModelSelector.NONE
        self.data_features_options = DataFeatureConfig(camera_conf=self.camera_option.rgb_sensor,
                                                       roi_selector=self.roi_selector,
                                                       size_estimation_selector=self.size_estimation_selector,
                                                       depth_selector=self.depth_option,
                                                       mass_selector=self.mass_estimation_option)

        self.simulator_config = PredictionsMetricsFrameworkConfig(self.dataset_manager_config,
                                                                  self.path_day_measures,
                                                                  self.data_features_options,
                                                                  self.mass_estimation_option,
                                                                  self.comparative_report_option)
        # ----------------------
        simulation = PredictionMetricsFramework(self.simulator_config)
        simulation.comparative_metrics_dataset_bbox(self.measures_selected_df)
        r = simulation.get_simulation_results()
        # ----------------------
        temporal_record = pd.DataFrame(
            [[self.camera_option.__name__(),
              self.roi_selector.name,
              self.size_estimation_selector.name,
              self.depth_option.name,
              self.mass_estimation_option.name,
              self.comparative_report_option.name,
              r.total_objects,
              r.unit_of_measurement,
              r.MSE,
              r.MAE,
              r.RMSE,
              r.MAPE,
              r.R2]],
            columns=self.headers_optimization)
        # ----------------------
        self.optimization_results_df = self.optimization_results_df.append(temporal_record, ignore_index=True)

    def bbox_simulation_method_2(self):
        self.roi_selector = ROISelector.BBOX
        self.size_estimation_selector = SizeEstimationSelector.BBOX
        self.depth_option = DepthSelector.MOD
        self.mass_estimation_option = MassEstimationModelSelector.NONE
        self.data_features_options = DataFeatureConfig(camera_conf=self.camera_option.rgb_sensor,
                                                       roi_selector=self.roi_selector,
                                                       size_estimation_selector=self.size_estimation_selector,
                                                       depth_selector=self.depth_option,
                                                       mass_selector=self.mass_estimation_option)

        self.simulator_config = PredictionsMetricsFrameworkConfig(self.dataset_manager_config,
                                                                  self.path_day_measures,
                                                                  self.data_features_options,
                                                                  self.mass_estimation_option,
                                                                  self.comparative_report_option)
        # ----------------------
        simulation = PredictionMetricsFramework(self.simulator_config)
        simulation.comparative_metrics_dataset_bbox(self.measures_selected_df)
        r = simulation.get_simulation_results()
        # ----------------------
        temporal_record = pd.DataFrame(
            [[self.camera_option.__name__(),
              self.roi_selector.name,
              self.size_estimation_selector.name,
              self.depth_option.name,
              self.mass_estimation_option.name,
              self.comparative_report_option.name,
              r.total_objects,
              r.unit_of_measurement,
              r.MSE,
              r.MAE,
              r.RMSE,
              r.MAPE,
              r.R2]],
            columns=self.headers_optimization)
        # ----------------------
        self.optimization_results_df = self.optimization_results_df.append(temporal_record, ignore_index=True)

    def bbox_simulation_method_3(self):
        self.roi_selector = ROISelector.BBOX
        self.size_estimation_selector = SizeEstimationSelector.BBOX
        self.depth_option = DepthSelector.MIN
        self.mass_estimation_option = MassEstimationModelSelector.NONE
        self.data_features_options = DataFeatureConfig(camera_conf=self.camera_option.rgb_sensor,
                                                       roi_selector=self.roi_selector,
                                                       size_estimation_selector=self.size_estimation_selector,
                                                       depth_selector=self.depth_option,
                                                       mass_selector=self.mass_estimation_option)

        self.simulator_config = PredictionsMetricsFrameworkConfig(self.dataset_manager_config,
                                                                  self.path_day_measures,
                                                                  self.data_features_options,
                                                                  self.mass_estimation_option,
                                                                  self.comparative_report_option)
        # ----------------------
        simulation = PredictionMetricsFramework(self.simulator_config)
        simulation.comparative_metrics_dataset_bbox(self.measures_selected_df)
        r = simulation.get_simulation_results()
        # ----------------------
        temporal_record = pd.DataFrame(
            [[self.camera_option.__name__(),
              self.roi_selector.name,
              self.size_estimation_selector.name,
              self.depth_option.name,
              self.mass_estimation_option.name,
              self.comparative_report_option.name,
              r.total_objects,
              r.unit_of_measurement,
              r.MSE,
              r.MAE,
              r.RMSE,
              r.MAPE,
              r.R2]],
            columns=self.headers_optimization)
        # ----------------------
        self.optimization_results_df = self.optimization_results_df.append(temporal_record, ignore_index=True)

    def bbox_simulation_method_4(self):
        self.roi_selector = ROISelector.BBOX
        self.size_estimation_selector = SizeEstimationSelector.BBOX
        self.depth_option = DepthSelector.MAX
        self.mass_estimation_option = MassEstimationModelSelector.NONE
        self.data_features_options = DataFeatureConfig(camera_conf=self.camera_option.rgb_sensor,
                                                       roi_selector=self.roi_selector,
                                                       size_estimation_selector=self.size_estimation_selector,
                                                       depth_selector=self.depth_option,
                                                       mass_selector=self.mass_estimation_option)

        self.simulator_config = PredictionsMetricsFrameworkConfig(self.dataset_manager_config,
                                                                  self.path_day_measures,
                                                                  self.data_features_options,
                                                                  self.mass_estimation_option,
                                                                  self.comparative_report_option)
        # ----------------------
        simulation = PredictionMetricsFramework(self.simulator_config)
        simulation.comparative_metrics_dataset_bbox(self.measures_selected_df)
        r = simulation.get_simulation_results()
        # ----------------------
        temporal_record = pd.DataFrame(
            [[self.camera_option.__name__(),
              self.roi_selector.name,
              self.size_estimation_selector.name,
              self.depth_option.name,
              self.mass_estimation_option.name,
              self.comparative_report_option.name,
              r.total_objects,
              r.unit_of_measurement,
              r.MSE,
              r.MAE,
              r.RMSE,
              r.MAPE,
              r.R2]],
            columns=self.headers_optimization)
        # ----------------------
        self.optimization_results_df = self.optimization_results_df.append(temporal_record, ignore_index=True)

    def bbox_simulation_method_5(self):
        self.roi_selector = ROISelector.BBOX
        self.size_estimation_selector = SizeEstimationSelector.BBOX
        self.depth_option = DepthSelector.CENTROID
        self.mass_estimation_option = MassEstimationModelSelector.NONE
        self.data_features_options = DataFeatureConfig(camera_conf=self.camera_option.rgb_sensor,
                                                       roi_selector=self.roi_selector,
                                                       size_estimation_selector=self.size_estimation_selector,
                                                       depth_selector=self.depth_option,
                                                       mass_selector=self.mass_estimation_option)

        self.simulator_config = PredictionsMetricsFrameworkConfig(self.dataset_manager_config,
                                                                  self.path_day_measures,
                                                                  self.data_features_options,
                                                                  self.mass_estimation_option,
                                                                  self.comparative_report_option)
        # ----------------------
        simulation = PredictionMetricsFramework(self.simulator_config)
        simulation.comparative_metrics_dataset_bbox(self.measures_selected_df)
        r = simulation.get_simulation_results()
        # ----------------------
        temporal_record = pd.DataFrame(
            [[self.camera_option.__name__(),
              self.roi_selector.name,
              self.size_estimation_selector.name,
              self.depth_option.name,
              self.mass_estimation_option.name,
              self.comparative_report_option.name,
              r.total_objects,
              r.unit_of_measurement,
              r.MSE,
              r.MAE,
              r.RMSE,
              r.MAPE,
              r.R2]],
            columns=self.headers_optimization)
        # ----------------------
        self.optimization_results_df = self.optimization_results_df.append(temporal_record, ignore_index=True)


    def test_run_simulation(self):
        # ------------------------
        # all tests are based on the camera and report selector
        self.camera_option = AzureKinect()
        self.comparative_report_option = ComparativeMeasuresReportSelector.A1
        # ------------------------
        # BOUNDING BOX
        self.bbox_simulation_method_1()
        self.bbox_simulation_method_2()
        self.bbox_simulation_method_3()
        self.bbox_simulation_method_4()
        self.bbox_simulation_method_5()
        # ------------------------
        # save final result
        self.optimization_results_df.to_csv(self.path_optimization, float_format='%.2f', sep=';')
        print(self.path_optimization)
        # ------------------------
        self.assertEqual('OK', 'OK')


if __name__ == '__main__':
    unittest.main()
