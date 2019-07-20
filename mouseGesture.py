from pynput.mouse import Button,Controller
mouse=Controller()
import cv2
v=cv2.VideoCapture(0)

while True:
    s,i=v.read()
    i=i[:,::-1,:]
    i=cv2.resize(i,(1920,1080))
    j=i[:,:,1]
    k=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    g=cv2.subtract(j,k)
    g=cv2.multiply(g,3)
    ret,thresh=cv2.threshold(g,80,255,cv2.THRESH_BINARY)
    thresh=cv2.resize(thresh,(1920,1080))
    contours,hie=cv2.findContours(thresh,0,1)
    
    area=[]
    for cnt in contours:
        a=cv2.contourArea(cnt)
        area.append(a)
        mx=max(area)
        ind=area.index(mx)
    if(len(contours)>0):
        try:
            cv2.drawContours(i,contours[ind],-1,(0,0,255),5)
            M=cv2.moments(contours[ind])
            global cx
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            cv2.circle(i,(cx,cy),10,(0,0,255),2)
            mouse.position=(cx,cy)
        
        except ZeroDivisionError as e:
            print(e)
    
    cv2.imshow('Normal Video',i)
    #cv2.imshow('Thresh Video',thresh)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
v.release()
