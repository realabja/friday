import cv2
import time

# define a video capture object
vid = cv2.VideoCapture(0)

while (True):
    time.sleep(0.1)
    ret, frame = vid.read()
    output =  frame.copy()

    rectangles = [(40, 40, 100,100)]

    for rect in rectangles:
        cv2.rectangle(output, (rect[0], rect[1]), (60, 60),(255,12,122), 10)



    cv2.imshow('input', frame)
    cv2.imshow('output', output)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()