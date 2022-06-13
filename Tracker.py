import cv2
import urllib.request
import numpy as np
import time
def nothing(x):
    pass

url='http://192.168.52.146/cam-mid.jpg'
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
l_h, l_s, l_v = 52, 35, 0
u_h, u_s, u_v = 76, 255, 255
cx2=0
cy2=0
vx2=0
vy2=0
pfile=open("Data_csv\Position.csv", "a")
vfile=open("Data_csv\Velocity.csv", "a")
afile=open("Data_csv\Acceleration.csv", "a")
pfile.write(time.strftime('%Y-%m-%d %I:%M:%S %p  Position Record Start \n', time.localtime(time.time())))
vfile.write(time.strftime('%Y-%m-%d %I:%M:%S %p  Velocity Record Start \n', time.localtime(time.time())))
afile.write(time.strftime('%Y-%m-%d %I:%M:%S %p  Acceleration Record Start \n', time.localtime(time.time())))
starttime=time.time()
while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    mask = cv2.inRange(hsv, l_b, u_b)
 
    cnts, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 
    for c in cnts:
        area=cv2.contourArea(c)
        
        if area>2000:
            newtime=time.time()
            t=str(newtime-starttime)+','
            cv2.drawContours(frame,[c],-1,(255,0,0),3)
            M=cv2.moments(c)
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])
            cxy=str(cx)+','+str(cy)
            pfile.write(t+cxy)
            pfile.write("\n")
            vx=cx-cx2
            vy=cy-cy2
            ax=vx-vx2
            ay=vy-vy2
            vxy=str(vx)+','+str(vy)
            axy=str(ax)+','+str(ay)
            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame,cxy,(cx-20, cy-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
            print("V : ",vx,', ',vy)
            vfile.write(t+vxy)
            vfile.write("\n")
            print("A : ",ax,', ',ay)
            afile.write(t+axy)
            afile.write("\n")
            cx2=int(cx)
            cy2=int(cy)
            vx2=int(vx)
            vy2=int(vy)
            
        
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("live transmission", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
        afile.close()
        vfile.close()
        pfile.close()
    
 
cv2.destroyAllWindows()