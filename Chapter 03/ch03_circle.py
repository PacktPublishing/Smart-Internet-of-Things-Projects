import cv2
import numpy as np


print('load image')
orig = cv2.imread('circle.png')
processed = cv2.imread('circle.png', 0)
processed = cv2.medianBlur(processed, 19)

print('processing...')
# param1 & param2 based on paper
# http://www.bmva.org/bmvc/1989/avc-89-029.pdf
circles = cv2.HoughCircles(processed, cv2.HOUGH_GRADIENT, 1, 70,
              param1=30,
              param2=15,
              minRadius=0,
              maxRadius=50)


circles = np.uint16(np.around(circles))
for (x, y, r) in circles[0, :]:
    cv2.circle(orig, (x, y), r, (0, 255, 0), 2)


print('completed')
print('writing to a file..')
cv2.imwrite('circle_process.png', orig)
print('done')
