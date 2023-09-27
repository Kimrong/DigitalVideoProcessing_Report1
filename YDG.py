import cv2 as cv
import numpy as np
import time


cap1 = cv.VideoCapture('./data/matrix.mp4')
ret1, frame1=cap1.read()
cap2 = cv.VideoCapture('./data/matrix.mp4')
ret2, frame2=cap2.read()
brightened_image=frame2
alpha=0.0
current_position = 0

frame_count = int(cap1.get(cv.CAP_PROP_FRAME_COUNT))
fps = int(cap1.get(cv.CAP_PROP_FPS))

print(fps)
print(frame_count)

def update_brightness(brightness):
    global brightened_image
    global alpha
    alpha = brightness / 10.0
    # 밝기 조절
    brightened_image = cv.convertScaleAbs(frame2, alpha=alpha, beta=0)
    # 조절된 영상 표시
    
def on_trackbar_change(pos):
    global current_position
    current_position = pos
    
def show():
    global frame1
    global frame2
    global ret1
    global ret2
    global alpha
    global current_position
    initial_brightness = 10
    time1=time.time()
    merged_image = cv.hconcat([frame1, frame2])
    cv.imshow('aaa',merged_image)
    cv.createTrackbar('Brightness', 'aaa', initial_brightness, 20, update_brightness)
    cv.createTrackbar('Position', 'aaa', 0, int(frame_count), on_trackbar_change)
    while ret1 or ret2:
        ret1, frame1=cap1.read()
        ret2, frame2=cap2.read()
        frame2 = cv.convertScaleAbs(frame2, alpha=alpha, beta=0)
        current_position=current_position+1
        cv.setTrackbarPos('Position', 'aaa', current_position)
        cap1.set(cv.CAP_PROP_POS_FRAMES, current_position)
        cap2.set(cv.CAP_PROP_POS_FRAMES, current_position)
        merged_image = cv.hconcat([frame1, frame2])
        cv.imshow('aaa',merged_image)
        cv.waitKey(1)
        time.sleep(0.018)
        
    print(time.time()-time1)

def main():
    show()
    
if __name__=="__main__":
    main()