__author__ = "Tommaso Tocci"
__email__ = "tommaso.tocci@outlook.it"

from function import leaf_detect
import os
import cv2
from tqdm import tqdm
from tkinter import filedialog
from tkinter import *

os.system('cls')

print('LEAF DETECTOR AND ANALYZER\n')

root = Tk()
root.withdraw()

path = filedialog.askdirectory()

calibration = float(input('Calibration Factor [mm/px] -> '))

totalFiles = 0

for _, _, files in os.walk(path):
    for Files in files:
        totalFiles += 1

ver = 'n'

while ver == 'n':

    os.system('cls')

    print('LEAF DETECTOR AND ANALYZER\n')

    low_tresh = int(input('Low threshold value -> '))
    high_tresh= int(input('High threshold value -> '))

    lf = leaf_detect(calibration,low_tresh,high_tresh)
    
    img = cv2.imread(os.path.join(path,'0.jpg'))

    lf.elaborate(img)
    lf.plot()

    ver = input('Continue? [y/n] -> ')

    if ver == 'y':
        break

os.system('cls')
print('LEAF DETECTOR AND ANALYZER\n')

pbar = tqdm(total=totalFiles)

for i in range(0,totalFiles):

    img = cv2.imread(os.path.join(path,'%i.jpg'%i))

    area,r,g,b = lf.elaborate(img)

    lf.update_dataframe(i)

    pbar.update()

pbar.close() 

df = lf.save_dataframe(path)



