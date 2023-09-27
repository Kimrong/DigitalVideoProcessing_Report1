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

def update_brightness(brightness):
    global brightened_image
    global alpha
    # 현재 화면에서 트랙바 값 받아오기 (0에서 100 사이)
    alpha = brightness / 10.0
    # 밝기 조절
    brightened_image = cv.convertScaleAbs(frame2, alpha=alpha, beta=0)
    # 조절된 영상 표시

    
def show():
        global frame1
        global frame2
        global ret1
        global ret2
        global alpha
        initial_brightness = 10
        time1=time.time()
        merged_image = cv.hconcat([frame1, frame2])
        cv.imshow('aaa',merged_image)
        cv.createTrackbar('Brightness', 'aaa', initial_brightness, 20, update_brightness)
        while ret1 or ret2:
            ret1, frame1=cap1.read()
            ret2, frame2=cap2.read()
            brightened_image = cv.convertScaleAbs(frame2, alpha=alpha, beta=0)
            merged_image = cv.hconcat([frame1, brightened_image])
            cv.imshow('aaa',merged_image)
            cv.waitKey(1)
            time.sleep(0.028)
        print(time.time()-time1)

def main():
    show()
    
if __name__=="__main__":
    main()