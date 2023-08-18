"""
Project: TorchVision 0.3 Object Detection Finetuning Tutorial
Author: Juan Carlos Miranda
Date: December 2021
Description:
 Adapted from https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
...

Use:
 python -m unittest ./tests/test_object_detector
 test_object_detector.TestStringMethods.test_object_detection_api

"""

import os
import time
import cv2
from detector.obj_detector_frame import ObjectDetectorFrame


def main_loop_webcam():
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 1)

    BASE_DIR = os.path.abspath('.')
    ################################
    # config for files models
    #home_user = os.path.join('/', 'home', 'usuario')
    home_user = os.path.join('C:', '\\', 'Users', 'Usuari')
    #main_path_project = os.path.join(home_user, 'development', 'object_detector')

    main_path_project = os.path.abspath('.')
    trained_model_folder = 'trained_model'
    trained_model_path = os.path.join(main_path_project, trained_model_folder)
    file_name_model = 'MODEL_SAVED.pth'
    file_model_path = os.path.join(trained_model_path, file_name_model)
    ################################
    time_1 = time.time()
    obj_detector = ObjectDetectorFrame(file_model_path)
    time_2 = time.time()
    time_total = time_2 - time_1
    print('load ObjectDetectorFrame time_total-->', time_total)
    a_threshold = 0.7
    # -----------------------------
    while True:
        ret, frame = cap.read()
        # cv2.imshow('webcam feed', frame)
        # ----------------------------
        # make something with frame
        # ----------------------------
        image_analyzed = obj_detector.object_detection_in_frame(frame, a_threshold)
        # ----------------------------
        if image_analyzed is None:
            cv2.imshow('webcam feed', frame)
        else:
            cv2.imshow('webcam feed', image_analyzed)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    # close camera
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main_loop_webcam()
