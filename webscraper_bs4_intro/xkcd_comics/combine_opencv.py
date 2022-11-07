import cv2
import numpy as np

img1 = 'wirecutter_recommendation.png'
img2 = 'konigsberg.png'
combined = 'combined.png'

img1Read = cv2.imread(img1)
img2Read = cv2.imread(img2)

# combinedImg = np.concatenate((img1Read, img2Read), axis=0)
h1, w1 = img1Read.shape[:2]
h2, w2 = img2Read.shape[:2]

#create empty matrix
combinedImg = np.zeros((h1+h2, max(w1, w2), 3), np.uint8)

#combine 2 images
combinedImg[:h1, :w1, :3] = img1Read
combinedImg[h1:h1+h2, :w2, :3] = img2Read

cv2.imwrite(combined, combinedImg)

# cv2.imshow('color image', combinedImg)
# cv2.waitKey(0)