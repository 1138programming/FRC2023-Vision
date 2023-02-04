import cv2
import cv2 as cv
import glob
import numpy as np
import os


chessboardSize = (8,8)
frameSize = (640,480)
ret, corners = cv.findChessboardCorners(chessboardSize, None)
img = ('C:\Users\eeuser\Desktop\apriltag\FRC2023-Vision\img left(8, 8)NoneFalse0.png')
draw = cv.drawChessboardCorners(img, chessboardSize, corners, ret)
cv2.drawChessboardCorners(img, draw)
cv2.imwrite('C:\Users\eeuser\Desktop\apriltag\FRC2023-Vision\img left(8, 8)NoneFalse0.png')

cv2.destroyAllWindows