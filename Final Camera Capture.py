import cv2
import cv2 as cv
import glob
import numpy as np

cap = cv2.VideoCapture(0)

num = 0

chessboardSize = (7,7)
frameSize = (640,480)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp [:,:2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1,2)

objpoints = [] # 3D points in the real world space
imgpoints = [] # 2D points in image plane
prev_img_shape = None

while cap.isOpened():
    succes1, img = cap.read()
    
    k = cv2.waitKey(5)
    
    if k == 27:
        break
    elif k == ord('s'):
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, chessboardSize, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
        cv2.imshow("Gray Image", gray)
        cv2.waitKey(6000)
        cv2.destroyWindow("Gray Image")
        cv2.waitKey(1000)
        
        result = cv2.imwrite("Gray Image" + str(num) + '.png', gray)
        if result == True:
            images = glob.glob("Gray Image" +  str(num) + '.png')
            print("File Saved Sucessfully")
        else:
            print("ERROR")
        num += 1
                    
    cv2.imshow('Camera', img)
    
cap.release()
                
cv2.destroyAllWindows()
                    