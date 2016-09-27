import numpy as np
import cv2


img = cv2.imread('circle.png')
cv2.imshow('My photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

