import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

img = cv2.imread('GreenCards1.jpg')
print(img)
cv2.imshow('cards', img)
cv2.waitKey(0)
cv2.destroyAllWindows()