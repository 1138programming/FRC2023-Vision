import cv2
import cv2 as cv
import glob
import numpy as np
import os

cap = cv2.VideoCapture(0)
	
num=0

chessboardSize = (8,8)
frameSize = (640,480)


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
        ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', gray)
        cv2.imshow("Distortion photo", img)
        cv2.imshow("Gray Distortion", gray)
        result=cv2.imwrite("Gray Distortion" + str(num) + '.png', gray)
        if result==True:
            print("File saved successfully")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.waitKey(1000)
            if ret == True:
        
                objpoints.append(objp)
        
                corners = cv.cornerSubPix(gray, corners, (11, 11), (-1,-1), criteria)
                imgpoints.append(corners)
        
        
                # Draw and display the corners
                cv.drawChessboardCorners(img, chessboardSize, corners, ret)
                cv.imshow('img left', img)
                cv.waitKey(1000)
        else:
            print("ERROR")
        num += 1
        cv2.waitKey(6000)
        cv2.destroyWindow("Distortion photo")
        cv2.destroyWindow("Gray Distortion")
        
    cv2.imshow('Test Cam',img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()