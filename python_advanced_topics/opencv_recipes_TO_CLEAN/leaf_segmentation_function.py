import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os

class leaf_detect():

    def __init__(self,calibration,low_tresh,high_tresh):

        self.calibration = calibration
        self.low_tresh = low_tresh
        self.high_tresh = high_tresh

        data = {'area':[1],'R':[1],'G':[1],'B':[1]}

        self.df = pd.DataFrame(data, columns=['area','R','G','B'])

    def elaborate(self,img):

        self.img = img
        
        self.img_filt = cv2.bilateralFilter(img,20,100,75)

        img_hsv = cv2.cvtColor(self.img_filt, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img_hsv, (self.low_tresh, 5, 5), (self.high_tresh, 255,255))

        imask = mask>0
        self.img_mask = np.zeros_like(img, np.uint8)
        self.img_mask[imask] = img[imask]

        gray = cv2.cvtColor(self.img_mask, cv2.COLOR_BGR2GRAY)
        _, threshed = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        contours,_ = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cmax = max(contours, key = cv2.contourArea) 
        epsilon = 0.002 * cv2.arcLength(cmax, True)
        self.approx = cv2.approxPolyDP(cmax, epsilon, True)
      
        width, height,_ = self.img_mask.shape
        filter = np.zeros([width, height,3],dtype=np.uint8)
        
        cv2.fillPoly(filter, pts =[cmax], color=(255,255,255))
    
        self.img_mask *= (filter//255)

        #AREA

        area_pix = self.calibration**2

        num_pix = cv2.countNonZero(cv2.cvtColor(self.img_mask, cv2.COLOR_BGR2GRAY))

        self.area = area_pix*num_pix

        #MEDIA

        r,g,b = cv2.split(cv2.cvtColor(self.img_mask, cv2.COLOR_BGR2RGB))

        self.mean_r = np.average(r,weights=(r>0))
        self.mean_g = np.average(g,weights=(r>0))
        self.mean_b = np.average(b,weights=(r>0))

        return self.area,self.mean_r,self.mean_g,self.mean_b

    def update_dataframe(self,index):

        self.df.loc[index] = [self.area,self.mean_r,self.mean_g,self.mean_b]

    def save_dataframe(self,path):

        self.df.to_excel(os.path.join(path,'out.xlsx'))

    def plot(self):

        fig, (ax1, ax2, ax3) = plt.subplots(1,3)

        plt.suptitle('Total area: %.3f mm^2\nMean Value: R-channel = %.1f G-channel = %.1f B-channel = %.1f'%(self.area,self.mean_r,self.mean_g,self.mean_b))

        ax1.imshow(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        ax1.set_title('Original')
        ax1.axis('off')
        cv2.drawContours(self.img_filt, [self.approx], -1, (0, 0, 255), 3)
        ax2.imshow(cv2.cvtColor(self.img_filt, cv2.COLOR_BGR2RGB))
        ax2.set_title('Filtered')
        ax2.axis('off')
        ax3.imshow(cv2.cvtColor(self.img_mask, cv2.COLOR_BGR2RGB))
        ax3.set_title('Mask')
        ax3.axis('off')

        plt.tight_layout()

        plt.show()
