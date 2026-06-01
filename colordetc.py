import cv2
from PIL import Image
from limits import get_limits

yellow = [0,255,255]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #HSV convert
    low , up = get_limits(color = yellow) 
    mask = cv2.inRange(hsvimg,low,up) #image masking by color limits
    mask1 = Image.fromarray(mask) 
    box = mask1.getbbox() #bounding box
    if box is not None:
        x1,y1,x2,y2 = box
        frame = cv2.rectangle(frame, (x1,y1),(x2,y2),(255,255,0),2) 
    
    cv2.imshow('cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()