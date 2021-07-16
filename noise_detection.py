import numpy as np
import cv2

noise = cv2.boxFilter(noise, cv2,CV_32F, (1,5))
b = np.var(b)

print (b)