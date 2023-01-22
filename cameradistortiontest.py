import cv2 as cv
import numpy as np
import glob


#####FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS#########

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
imgpointsL = [] # 2d points in image plane
imgpointsR = [] # 2d points in image plane


imagesLeft = sorted(glob.glob('images/stereoLeft/*.png'))
imagesRight = sorted(glob.glob('images/stereoRight/*.png'))

for imgLeft, imgRight in zip(imagesLeft, imagesRight):
    
    imgL = cv.imread(imgLeft)
    imgR = cv.imread(imgRight)
    grayL = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)
    grayR = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)
    
    
    # Find the chessbooard corners
    retL, cornersL = cv.findChessboardCorners(grayL, chessboardSize, None)
    retR, cornersR = cv.findChessboardCorners(grayR, chessboardSize, None)
    
    # If found, add objects points, image points (after refining them)
    if retL and retR == True:
        
        objpoints.append(objp)
        
        cornersL = cv.cornerSubPix(grayL, cornersL, (11, 11), (-1,-1), criteria)
        imgpointsL.append(cornersL)
        
        cornersR = cv.cornerSubPix(grayR, cornersR, (11, 11), (-1,-1), criteria)
        imgpointsL.append(cornersR)
        
        # Draw and display the corners
        cv.drawChessboardCorners(imgL, chessboardSize, cornersL, retL)
        cv.imshow('img left', imgL)
        cv.drawChessboardCorners(imgR, chessboardSize, cornersR, retR)
        cv.imshow('img right', imgR)
        cv.waitKey(1000)
            
cv.destroyAllWindows()

