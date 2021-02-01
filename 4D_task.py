#import libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

#open images 

image = cv2.imread('Desktop/interview/CV Test/StarMap.png', 0)
image2 = image.copy()
tpl = cv2.imread('Desktop/interview/CV Test/Small_area_rotated.png', 0)
tpl2 = cv2.imread('Desktop/interview/CV Test/Small_area.png', 0)

def find_image(img, template):

  w, h = template.shape[::-1]
  img = img2.copy()
  method = eval('cv2.TM_SQDIFF')
  #image matching
  res = cv2.matchTemplate(img,template,method)
  #our values
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  #left side position
  top_left = min_loc
  #right side position
  bottom_right = (top_left[0] + w, top_left[1] + h)
  cv2.rectangle(img,top_left, bottom_right, 255, 2)
  #illustration  	
  plt.subplot(121),plt.imshow(res,cmap = 'gray')
  plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
  plt.subplot(122),plt.imshow(img,cmap = 'gray')
  plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
  plt.suptitle('Find Image') 
  plt.show()
  return f'coordinates : {min_loc}, {max_loc}'
  

#For rotated image
print(find_image(image2,tpl))

#For normal image
print(find_image(image2,tpl2))
