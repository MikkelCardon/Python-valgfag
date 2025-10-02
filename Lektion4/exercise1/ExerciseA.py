import numpy as np
a = np.array([1,2,3])
print (a)
import sys
print("The Python version is %s.%s.%s" % sys.version_info[:3])
import cv2
img = cv2.imread('opencv_hello.jpg', 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
