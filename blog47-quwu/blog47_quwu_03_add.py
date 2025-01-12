# -*- coding:utf-8 -*-
import cv2
import numpy as np

#读取图片
img = cv2.imread("fj.png", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

#加噪声
for i in range(50000):    
    x = np.random.randint(0, rows) 
    y = np.random.randint(0, cols)    
    img[x,y,:] = 210

cv2.imshow("noise", img)
           
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('fj-res.png',img)
