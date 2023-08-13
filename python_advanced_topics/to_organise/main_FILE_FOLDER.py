import os

if __name__ == '__main__':
    print("HELLO")
    # source directory
    source_dir = r"C:\Users\Usuari\PycharmProjects\SizeEstimation"  # put your directory here
    # output directory
    # output_path = r"C:\Users\Shubham\PycharmProjects\MSRegistration\SIFT_results_batch"
    images = []
    count = 0
    filenames_in_folder = os.listdir(source_dir)
    extension_file_to_search = '.tif'

    # Iterate through the folder
    for a_scene_name in os.listdir(source_dir):
        # get file name without extension
        print(f'a_scene_name->|{a_scene_name}|')
        if a_scene_name.endswith(extension_file_to_search):
            print(f'a_scene_name filtered={a_scene_name}')
            a_scene_name_str=a_scene_name[0:8] # for scene name

            ################
            # HERE MAKE SOMETHING WITH 1 TO 5
            # split here with underscore
            ################
            # again another search by filter with scene
            #
            x = a_scene_name.split("_")
            pass

#    if file not in images:
#        images.append(file)
#    count += 1

print(images)
