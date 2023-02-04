import pupil_apriltags as apriltag
import cv2
import numpy

cap = cv2.VideoCapture(0)
at_detector = apriltag.Detector(families='tag36h11')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

widthMid = int(width/2)
heightMid = int(height/2)
midwidth = (widthMid, 0)
botwidth = (widthMid, height)
leftheight = (heightMid, 0)
rightheight = (heightMid, width)

#vw = cv2.VideoWriter("test_video.mp4", fourcc, 30, (width, height))

while(1):
    # get image
    ret, frame = cap.read()
    # check keyboard
    k = cv2.waitKey(1)
    if k==27:
        break
    elif ret==0:
        print("ret==0")
        break
    # check apriltag
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    tags = at_detector.detect(gray)
    cv2.line(frame, (widthMid, 0), (widthMid, height), (187, 197, 57), 5)
    cv2.line(frame, (0, heightMid), (width, heightMid), (187, 197, 57), 5)
    for tag in tags:
        cv2.circle(frame, tuple(tag.corners[0].astype(int)), 4, (197, 187, 57), 5) # left-top
        cv2.circle(frame, tuple(tag.corners[1].astype(int)), 4, (197, 187, 57), 5) # right-top
        cv2.circle(frame, tuple(tag.corners[2].astype(int)), 4, (197, 187, 57), 5) # right-bottom
        cv2.circle(frame, tuple(tag.corners[3].astype(int)), 4, (197, 187, 57), 5) # left-bottom
        b = (tuple(tag.corners[0].astype(int))[0], tuple(tag.corners[0].astype(int))[1])
        c = (tuple(tag.corners[1].astype(int))[0], tuple(tag.corners[1].astype(int))[1])
        d = (tuple(tag.corners[2].astype(int))[0], tuple(tag.corners[2].astype(int))[1])
        a = (tuple(tag.corners[3].astype(int))[0], tuple(tag.corners[3].astype(int))[1])
    # show result
        cv2.line(frame, a, b, (58, 30, 196), 5, lineType=cv2.LINE_AA)
        cv2.line(frame, b, c, (58, 30, 196), 5, lineType=cv2.LINE_AA)
        cv2.line(frame, c, d, (58, 30, 196), 5, lineType=cv2.LINE_AA)
        cv2.line(frame, d, a, (58, 30, 196), 5, lineType=cv2.LINE_AA)
#    vw.write(frame)
    cv2.imshow('capture', frame)
    

cap.release()
#vw.release()
cv2.destroyAllWindows()
