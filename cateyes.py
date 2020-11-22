import cv2
import cvui

## perseption ##

## rtsp_username = "enter_username"
rtsp_password = "enter_password"
width = 800
height = 480
cam_no = 1
def create_camera (channel):
    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@192.168.11.110:554/Streaming/channels/" + channel + "02" #change the IP to suit yours
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    cap.set(3, 640)  # ID number for width is 3
    cap.set(4, 480)  # ID number for height is 480
    cap.set(10, 100)  # ID number for brightness is 10qq
    return cap
cam = create_camera(str(cam_no)) ##

cam1cap = cv.VideoCapture("rtsp://192.168.1.2:8080/out.h264") ##cv2.VideoCapture('rtsp://admin:123456@192.168.0.333')##

if (cap.isOpened() == False): 
print("Unable to read camera feed")

## width= int(cam1cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cam1cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) ##

width= int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
##out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))##

while True:
    ret,frame= video.read()

    writer.write(frame)
    ##out.write(frame)##
    path = 'D:/OpenCV/Scripts/ch1video'
path = 'D:/OpenCV/Scripts/Images'
cv2.imwrite(os.path.join(path , 'waka.jpg'), frame)

    cv2.imshow('frame', frame)
    ##cv2.imshow('Original', frame)##
    if cv2.waitKey(1) & 0xFF == 27:
        break


video.release()
writer.release()
cv2.destroyAllWindows()

