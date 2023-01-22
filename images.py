import cv2
import cv2 as cv
import glob
import numpy as np

cap = cv2.VideoCapture(0)

num=0

while cap.isOpened():

    succes1, img = cap.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', img)
        print("images saved!")
        num += 1

    cv2.imshow('Img 1',img)
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

    imagesLeft = sorted(glob.glob('images/stereoLeft/*.png'))
    for imgLeft in zip(imagesLeft):
    
        imgL = cv.imread(imgLeft)
        grayL = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)
    
    
        # Find the chessbooard corners
        retL, cornersL = cv.findChessboardCorners(grayL, chessboardSize, None)
    
        # If found, add objects points, image points (after refining them)
        if retL == True:
        
            objpoints.append(objp)
        
            cornersL = cv.cornerSubPix(grayL, cornersL, (11, 11), (-1,-1), criteria)
            imgpointsL.append(cornersL)
        
        
            # Draw and display the corners
            cv.drawChessboardCorners(imgL, chessboardSize, cornersL, retL)
            cv.imshow('img left', imgL)
            cv.waitKey(1000)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()