"""
Author: AUTHOR's NAME
Description:
    Creating a Pandas frame
    Adding records
    Saving in .CSV format


Usage:
    python activity_06_01.py
"""
import os
import pandas as pd


def main_function_01():
    """
    Creating Pandas dataframe with columns
    Adding record to fruit dataframe
    Saving dataframe in .CSV file
    Executing calculations over the dataset

    :return:
    """
    print("Pandas dataframe!!!")

    root_folder = os.path.abspath('.')  # folder in file system
    day_measures_filename = 'comparative_by_day.csv'
    path_to_save_df = os.path.join(root_folder, 'output_dataset')  # Folder to save .CSV
    path_day_measures = os.path.join(path_to_save_df, day_measures_filename)  # path with the name of the file

    # Creating Pandas dataframe with columns
    headers_day_comparative = ['fruit_id', 'lab.tree', 'lab.fruit_label', 'lab.caliber_mm', 'lab.height_mm', 'lab.weight_gr', 'lab.observations']
    fruit_df = pd.DataFrame([], columns=headers_day_comparative)

    # ----------------------------------------
    # Row preparation
    rows_set = [
        [2100, 3, 'APPLE_2100', 60.5, 61.2, 120.3, ''],
        [2101, 3, 'APPLE_2101', 60.5, 62.2, 121.3, 'Damaged'],
        [2102, 3, 'APPLE_2102', 61.5, 62.2, 122.3, 'Beaten fruit']
    ]

    one_row = [[2100, 3, 'APPLE_2100', 60.5, 61.2, 120.3, '']]
    # ----------------------------------------
    # Adding rows
    temporal_record_df = pd.DataFrame(rows_set, columns=headers_day_comparative)
    #temporal_record_df = pd.DataFrame(one_row, columns=headers_day_comparative)
    # ----------------------------------------

    # Adding record to fruit dataframe
    fruit_df = pd.concat([fruit_df, temporal_record_df], ignore_index=True)

    # Saving dataframe in .CSV file
    fruit_df.to_csv(path_day_measures, float_format='%.2f', sep=';')

    # Executing calculations
    total_weight = fruit_df['lab.weight_gr'].sum()
    mean_weight = fruit_df['lab.weight_gr'].mean()

    print(f"---------------------------")
    print(f"RESUME")
    print(f"---------------------------")
    print(f"total_weight={total_weight}")
    print(f"mean_weight={mean_weight}")


    # Open and read .CSV
    reading_fruit_df = pd.read_csv(path_day_measures, dtype=str, sep=';')

    pass




if __name__ == "__main__":
    # single-line comment here
    print("STARTING __main__!")
    print("Now calling to the main function --> main_function_01()")
    main_function_01()
    print("After the main function --> main_function_01()")
    pass
