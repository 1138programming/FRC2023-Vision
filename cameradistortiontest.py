import pupil_apriltags as apriltag
import cv2 as cv
import numpy as np
import glob

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 90, 0.001)

# prepare object points in the format of (x,y,z)
objp = np.zeros((8*8,3), np.float32)
objp [:,:2] = np.mgrid[0:8, 0:8].T.reshape(-1,2)

# Arrays to store object points and image points from all images in view of the camera
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane

images = glob.glob('*.jpg')

for fname in images:
    img = cv.imread(fname)
    gray = cv.cutColor(img,cv.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (8,8), None)
    
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        
        #Draw and display the corners
        cv.drawChessboardCorners(img, (8,8), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
        
cv.destroyAllWindows

"""
    
    Issues: wont's work on computer cam, have yet to try on webcam
    
"""