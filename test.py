import cv2
import numpy
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

color_hsv = {
    # We put HSV format of color here. 
    "cone": {'lower': numpy.array([15, 115, 70]), 'upper': numpy.array([25, 255, 245])},
    "cube": {'lower': numpy.array([100, 40, 40]), 'upper': numpy.array([120, 250, 250])},
}

while True:
    k = cv2.waitKey(1)
    if k==27:
        break
    res, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    median = cv2.medianBlur(hsv, 35)
    #gauss = cv2.GaussianBlur(hsv, (33, 33), 1)
    erode = cv2.erode(median, None, iterations=3)
    
    cone_hsv = cv2.inRange(erode, color_hsv['cone']['lower'], color_hsv['cone']['upper'])
    cube_hsv = cv2.inRange(erode, color_hsv['cube']['lower'], color_hsv['cube']['upper'])
    
    cone_thresh, cone_binary = cv2.threshold(cone_hsv, 100, 200, cv2.THRESH_BINARY)
    cone_contours, cone_hierarchy = cv2.findContours(cone_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    xo, yo, ho, wo = cv2.boxPoints(cone_binary)
    cv2.rectangle(cone_binary, (xo, yo), (xo+wo, yo+ho), (0, 255, 255), 3)
    cube_thresh, cube_binary = cv2.threshold(cube_hsv, 100, 200, cv2.THRESH_BINARY)
    cube_contours, cube_hierarchy = cv2.findContours(cube_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("cone",cone_binary)
    cv2.imshow("cube", cube_binary)



cap.realease()
cv2.destroyAllWindows()