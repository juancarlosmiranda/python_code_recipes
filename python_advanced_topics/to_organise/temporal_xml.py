# ------------------------------------------------------------------
    dataset_root_path = os.path.join(base_path, dataset_root_folder)
    dataset_images_path = os.path.join(dataset_root_path, images_sub_folder)
    dataset_annotations_path = os.path.join(dataset_root_path, annotations_sub_folder)
    dataset_squares_path = os.path.join(dataset_root_path, squares_sub_folder)

    # iterate over directory with data labelled
    annotated_csv_file_list = os.listdir(dataset_annotations_path)
    for an_annotated_csv_file_name in annotated_csv_file_list:
        an_annotated_csv_file_path = os.path.join(dataset_annotations_path, an_annotated_csv_file_name)
        an_annotated_base_name = an_annotated_csv_file_name.split(csv_extension)[0]

        # get image data info
        an_image_file_name = an_annotated_base_name + img_extension
        an_image_path = os.path.join(dataset_images_path, an_image_file_name)
        width = PIL.Image.open(an_image_path).size[0]
        height = PIL.Image.open(an_image_path).size[1]
        circles_df = pd.read_csv(an_annotated_csv_file_path, header=None)

        # here we create an xml header
        f = ET.Element("annotations")
        ET.SubElement(f, 'filename').text = an_image_file_name
        size_element = ET.SubElement(f, 'size')
        ET.SubElement(size_element, 'width').text = str(width)
        ET.SubElement(size_element, 'height').text = str(height)
        ET.SubElement(size_element, 'depth').text = "3"

        # iterate over labelled objects with Pychetlabeller
        for index, a_row in circles_df.iterrows():
            # get coordinates of marked object in one image
            xmin = int(a_row[1])
            xmax = int(a_row[1] + a_row[3])
            ymin = int(a_row[2])
            ymax = int(a_row[2] + a_row[4])

            # by each row make add to the XML tree
            object_element = ET.SubElement(f, 'object')
            ET.SubElement(object_element, 'name').text = class_label_name
            ET.SubElement(object_element, 'difficult').text = "0"
            bbox = ET.SubElement(object_element, 'bbox')
            xmin_xml = ET.SubElement(bbox, 'xmin')
            ymin_xml = ET.SubElement(bbox, 'ymin')
            xmax_xml = ET.SubElement(bbox, 'xmax')
            ymax_xml = ET.SubElement(bbox, 'ymax')
            # assign values and convert to string
            xmin_xml.text = str(xmin)
            ymin_xml.text = str(ymin)
            xmax_xml.text = str(xmax)
            ymax_xml.text = str(ymax)

        break
    # write body of xml and close the file
    filename = os.path.join(dataset_squares_path, an_annotated_base_name + ".xml")
    tree = ET.ElementTree(f)
    tree.write(filename, pretty_print=True)





# manage images
    #ones_ones_mask = cv2.adaptiveThreshold(ones_array_mask, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 0)

    # segmentation with mask 1 single threshold
    #ones_bit_mask = (temporal_depth_filter == True).astype('int')
    #mask_depth = depth_data * ones_array_mask

    # images names for mask 2
    #image_segmented_mask_name_2_2 = rgb_image_name + '_mask2.jpg'
    #image_name_heatmap_2_2 = depth_image_name + '_h_2_2.jpg'
    #path_depth_heatmap = os.path.join()

    # open masks
    #mask_frame = cv2.imread(self.mask_file_path, cv2.IMREAD_GRAYSCALE)
    #cv2.imshow('Mask ones', ones_ones_mask)
    #cv2.imshow('RGB masked', rgb_data_segmented_1)

