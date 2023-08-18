"""
Project:
Author:
Date:
Description:
It is an example to save data as .CSV and to load data from .CSV file
...

Use:
"""
import os
import pandas as pd

if __name__ == '__main__':
    print('Pandas Example')
    df_file_name = 'my_example.csv'

    headers_t = ['image_name', 'meanDepth', 'stdDepth', 'minDepth', 'maxDepth', 'modeDepth', 'sizePx', 'sizeMeasured',
                 'label_class']
    table_data_struct = {
        'image_name': [0.0, 0.0],
        'meanDepth': [0.0, 0.0],
        'stdDepth': [0.0, 0.0],
        'minDepth': [0.0, 0.0],
        'maxDepth': [0.0, 0.0],
        'modeDepth': [0.0, 0.0],
        'sizePx': [0.0, 0.0],
        'sizeMeasured': [0.0, 0.0],
        'label_class': ['label_1', 'label_2']
    }

    BASE_FOLDER = os.path.abspath('.')
    path_to_save_df = os.path.join(BASE_FOLDER, df_file_name)
    print(path_to_save_df)

    # df = pd.DataFrame(table_data_struct, columns=headers_t)
    # df.to_csv(path_to_save_df, sep=';')

    # READ FROM .CSV and load to DataFrame
    # data_df = pd.read_csv(path_to_save_df, sep=';')
    # df.describe()

    headers_resume_frame = ['n', 'label', 'measure_c_px', 'measure_h_px', 'caliber_estimation_mm',
                            'height_estimation_mm',
                            'mass_estimation gr']
    table_data_struct_2 = {'n':[],
                           'label':[],
                           'measure_c_px': [],
                           'measure_h_px': [],
                           'caliber_estimation_mm': [],
                           'height_estimation_mm': [],
                           'mass_estimation gr': []
                           }
    # record_by_obj_df = pd.DataFrame(table_data_struct_2)
    n = 0
    current_label = 'LABEL_1'
    measure_c_px = 91
    measure_h_px = 91
    caliber_estimation_mm = 80.2
    height_estimation_mm = 79
    result_mass_estimation = 200.1
    record_by_obj_df = pd.DataFrame([[n, current_label, measure_c_px, measure_h_px, caliber_estimation_mm,
                                      height_estimation_mm, result_mass_estimation]], columns=headers_resume_frame)

    #all_obj_df = pd.DataFrame(table_data_struct_2)
    all_frame_obj_df = pd.DataFrame([], columns=headers_resume_frame)
    all_frame_obj_df = all_frame_obj_df.append(record_by_obj_df, ignore_index=True)
    all_frame_obj_df = all_frame_obj_df.append(record_by_obj_df, ignore_index=True)
    print(record_by_obj_df)
    print(all_frame_obj_df)


    pass
