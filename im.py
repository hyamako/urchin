import cv2
import numpy as np
from datetime import datetime

if __name__=='__main__':
    cam = []
    ret = []
    frame = []
    for i in range(2):
        cam.append(cv2.VideoCapture(i))
        ret_t, frame_t = cam[i].read()
        ret.append(ret_t)
        frame.append(frame_t)

    b = True
    while True:
        now = datetime.now()
        fntime = lambda n : int(n.strftime('%M'))
        
        if(fntime(now) % 2 == 0):
            f = now.strftime('%Y-%m-%d-%H-%M-%S') + ".jpg"
            if b:
                for i in range(2):
                    f = now.strftime('%Y-%m-%d-%H-%M-%S') + str(i) + ".jpg"
                    cv2.imwrite(f,frame[i])
                    print("seve={},bool={},cam={}".format(f,b,i))
                b = False
        else:
            b = True
        
        cv2.imshow("Input",frame[0])
        key = cv2.waitKey(10)
        
        if key == 27:
            cv2.destroyAllWindows()
            break
