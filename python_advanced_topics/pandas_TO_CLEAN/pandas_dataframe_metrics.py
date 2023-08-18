"""
Project:
Author:
Date:
Description:
...

Use:
"""
import os


def loading_csv():
    BASE_FOLDER = os.path.abspath('.')
    day_measures_filename = 'day_measures.csv'
    path_to_save_df = os.path.join(BASE_FOLDER, 'output_dataset')
    path_day_measures = os.path.join(path_to_save_df, day_measures_filename)

    # create pandas dataframe with columns
    headers_day_measures = ['date_capture', 'time_capture', 'fruit_id', 'pred.obj_detection', 'pred.measure_c_px',
                            'pred.measure_h_px', 'pred.depth', 'pred.caliber_mm', 'pred.height_mm', 'pred.mass_gr']
    day_measures_df = pd.DataFrame([], columns=headers_day_measures)

    pass


if __name__ == '__main__':
    """
    Create .xml files from files generated in Pychetlabeler tagging. 
    """
    print("PRINT MAIN--")
    loading_csv()