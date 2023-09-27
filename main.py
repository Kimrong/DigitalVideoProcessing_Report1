import cv2 as cv
import time
import sys

#영상 경로와 이름
path="./data/"
name="frozen.mp4"
fullName=path+name

#영상 불러오기
cap1=cv.VideoCapture(fullName)
cap2=cv.VideoCapture(fullName)
if not cap1.isOpened() or not cap2.isOpened():
	sys.exit()

#딜레이 설정
fps = cap1.get(cv.CAP_PROP_FPS)
delay = 1000/(fps)

#영상 재생
success, frame = cap1.read()
margin = 1
while success:
    s = time.time()
    cv.imshow(name, frame)
    success, frame = cap1.read()
    cv.waitKey(1)
    while ( (time.time() - s) * 1000 ) < (delay - margin):
        pass

#메모리 반환
cap1.release()


