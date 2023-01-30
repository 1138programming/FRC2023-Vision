# import required libraries
import cv2

# read input image
img = cv2.imread('Gray Distortion0.png')

# convert the input image to a grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (8,8),None)

# if chessboard corners are detected
if ret == True:
   print("true")
   # Draw and display the corners
   img = cv2.drawChessboardCorners(img, (8,8), corners,ret)
   cv2.imshow('Chessboard',img)
   cv2.waitKey(0)
else: 
    print("ERROR")
cv2.destroyAllWindows()