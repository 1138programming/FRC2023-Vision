import cv2
import cv2 as cv
import numpy as np
import glob
import os

cap = cv2.VideoCapture(0)
num = 0
image = cv2.imread('1.jpg',1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


while cap.isOpened():
    
    k = cv2.waitKey(5)
    
    if k == 27:
        break
    elif k == ord('c'): # wait for 'c' key to save and exit
        

        num += 1
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
        objpoints = [] # 3d points in the real world space
        imgpoints = [] # 2d points in image plane
        
        imagesCaptured = sorted(glob.glob())
        for images in zip(imagesCaptured):
            
            img = cv.imread(images)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            
            # Find the chessboard corners
            ret, corners, = cv.findChessboardCorners(gray, chessboardSize, None)
            
            # If found add object points, image points (after refining them)
            if ret == True:
                
                objpoints.append(objp)
                
                corners = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                imgpoints.append(corners)
                
                # Draw and display the corners
                cv.drawChessboardCorners(img, chessboardSize, corners, ret)
                cv.imshow('imgCap', img)
                cv.waitKey(1000)        
                cv2.imwrite(os.path.join('1' + str(num) + '.jpg'), img)
                cv2.imshow("Distortion photo", img)
                cv2.waitKey(6000)
                cv2.destroyWindow("Distortion photo")
                result=cv2.imwrite(os.path.join('1' + str(num) + '.jpg'), img)
                if result==True:
                    print("File saved successfully")
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('Gray image', gray)
                else:
                    print("images saved!")

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows