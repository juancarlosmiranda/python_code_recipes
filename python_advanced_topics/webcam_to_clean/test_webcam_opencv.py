"""
Project: TorchVision 0.3 Object Detection Finetuning Tutorial
Author: Juan Carlos Miranda
Date: December 2021
Description:
 Adapted from https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
...

Use:
 python -m unittest ./test/test_object_detector
 test_object_detector.TestStringMethods.test_object_detection_api

"""

import os
import time
import cv2



def main_loop_webcam():
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    #cap.set(cv2.CAP_PROP_FPS, 1)
    # -----------------------------
    while True:
        ret, frame = cap.read()
        # cv2.imshow('webcam feed', frame)
        # ----------------------------
        # make something with frame
        # ----------------------------
        #image_analyzed = obj_detector.object_detection_in_frame(frame, a_threshold)
        # ----------------------------
        cv2.imshow('webcam feed', frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    # close camera
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main_loop_webcam()
