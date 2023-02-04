import numpy as np
import cv2
import glob

# prepare object points
#Enter the number of inside corners in x
nx = 8
#Enter the number of inside corners in y
ny = 8
# Make a list of calibration images
chess_images = glob.glob('Gray Distortion0.png')
# Select any index to grab an image from the list
for i in range(len(chess_images)):
    # Read in the image
    chess_board_image = cv2.imread(chess_images[i])
    # Convert to grayscale
    gray = cv2.cvtColor(chess_board_image, cv2.COLOR_RGB2GRAY)
    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(chess_board_image, (nx, ny), None)
    # If found, draw corners
    if ret == True:
        # Draw and display the corners
        cv2.drawChessboardCorners(chess_board_image, (nx, ny), corners, ret)
        result_name = 'board'+str(i)+'.jpg'
        cv2.imwrite(result_name, chess_board_image)