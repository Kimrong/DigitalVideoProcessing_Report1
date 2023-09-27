import cv2 as cv
import time

#이름과 경로
path="./data/"
name="matrix.mp4"
fullname=path+name
winname=name[0:-4]

#영상 불러오기
cap1 = cv.VideoCapture(fullname)
cap2 = cv.VideoCapture(fullname)
ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()

#프레임 관련 변수
tot_frame = int(cap1.get(cv.CAP_PROP_FRAME_COUNT))
fps=int(cap1.get(cv.CAP_PROP_FPS))
bias=10
delay=int(1000/fps)-bias

#화면에 프레임을 표시하기 위한 변수
text_pos = (20, 40)  # 텍스트가 추가될 좌표 (x, y)
font = cv.FONT_HERSHEY_SIMPLEX  # 폰트 선택
font_scale = 1  # 폰트 크기
font_color = (0, 0, 254)  # 폰트 색상 (BGR 형식)
font_thickness = 2  # 폰트 두께

if cap1.isOpened() and cap2.isOpened():
    while ret1 or ret2:
        #현재 프레임 띄우기
        text_frame_1 = cv.putText(frame1, str(int(cap1.get(cv.CAP_PROP_POS_FRAMES))), text_pos, font, font_scale, font_color,
                                  font_thickness)
        text_frame_2 = cv.putText(frame2, str(int(cap2.get(cv.CAP_PROP_POS_FRAMES))), text_pos, font, font_scale,
                                  font_color, font_thickness)
        #프레임 합쳐서 윈도우에 띄우기
        merged_image = cv.hconcat([text_frame_1, text_frame_2])
        # 이미지에 텍스트 추가

        cv.imshow(winname,merged_image)

        #"esc"로 종료, "space"로 일시정지
        key = cv.waitKey(delay)
        if key==27:
            break
        elif key==32:
            while True:
                key = cv.waitKey()
                if key==32:
                    break

        #프레임 받아오기
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

