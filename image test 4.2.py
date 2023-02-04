import cv2
import cv2 as cv
import glob
import numpy as np

cap = cv2.VideoCapture(0)

num=0

chessboardSize = (7,7)
frameSize = (640,480)

# Enter the number of inside corners in x
nx = 7

# Enter the number of inside corners in y
ny = 7

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points in the format of (x,y,z)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp [:,:2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm

# Arrays to store object points and image points from all images in view of the camera
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane

while cap.isOpened():
    succes1, img = cap.read()
    
    k = cv2.waitKey(5)
    
    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, chessboardSize, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
        cv2.imshow("Distortion photo", img)
        cv2.imshow("Gray Distortion", gray)
        cv2.waitKey(6000)
        cv2.destroyWindow("Distortion photo")
        cv2.destroyWindow("Gray Distortion")
        cv2.waitKey(1000)
        
        draw = cv.drawChessboardCorners(img, chessboardSize, corners, ret)
        result = cv2.imwrite("Gray Distortion" + str(num) + '.jpg', gray)
        if result == True:
            cv2.imwrite("Gray Distortion" + str(num) + '.png', draw)
            print("File saved successfully")
            cv2.waitKey(6000)
            
        else:
            print("ERROR")
        num += 1
        cv2.waitKey(6000)
        
    cv2.imshow('Test Cam', img)
    
# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows