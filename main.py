import cv2 as cv
import os 
from datetime import datetime

# 웹켐 연결 (0은 기본 웹켐이며, 1,2, 등으로 외장카메라 연결 하는 기능)
capture = cv.VideoCapture(0)

# 영상 코덱을 설정, XVID 는 .avi파일에서 자주 쓰는 코덱
fourcc = cv.VideoWriter_fourcc(*'XVID')

out = None
recording = False   # 녹화 여부
start_time = None   # 녹화의 시작시간

contrast = 1.0      # 밝기
brightness = 0      # 대비

#경로 > 바탕화면 굿
path = os.path.join(os.path.expanduser("~"), "Desktop")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

text_queue = []

while True:
    # ret : 읽기 성공 여부 
    # frame = 실제 이미지 데이터 (numpy 배열을 통해 받아옴, 행렬개념으로 이해하면 아주 굿)
    ret, frame = capture.read()
    frame = cv.flip(frame,1)
    frame = cv.convertScaleAbs(frame, alpha = contrast, beta = brightness)
    display_frame = frame.copy()
    
    current_time = datetime.now()
    new_queue = []
    for text , start in text_queue:
        elapsed = (current_time - start).total_seconds()
        if elapsed < 1:
            cv.putText(display_frame, text, (10,30), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
            new_queue.append((text,start))
    text_queue = new_queue
    
    # 카메라 읽기 실패하면 break
    if not ret:
        break
    
    if recording:
        elapsed = int((datetime.now() - start_time).total_seconds())
        hours = elapsed//3600
        minutes = elapsed % 3600 // 60
        seconds = elapsed % 60
        h, w = frame.shape[:2]
        # putText(표시할 영상, 표시할 글자{녹화시간}, 위치, 폰트, 글자 크기, 색상(이거 RGB BGR임 제발 헷갈리지말기), 글자 두께)
        cv.putText(display_frame, f"REC {hours:02d}:{minutes:02d}:{seconds:02d}", (10,h-10), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
    
    # ishow : 화면출력
    cv.imshow("Webcam", display_frame)
    key = cv.waitKey(1) & 0xFF
               
    if key in [ord('<'), ord(',')]:
        contrast -= 0.1
        text_queue.append((f"Contrast : {contrast:.1f}", datetime.now()))
    elif key in [ord('>'), ord('.')]:
        contrast += 0.1
        text_queue.append((f"Contrast : {contrast:.1f}", datetime.now()))
    elif key in [ord('['), ord('{')]:
        brightness -= 10
        text_queue.append((f"Brightness : {brightness}", datetime.now()))
    elif key in [ord(']'), ord('}')]:
        brightness += 10
        text_queue.append((f"Brightness : {brightness}", datetime.now()))
    elif key == ord('r'):
        contrast = 1.0
        brightness = 0
        text_queue.append((f"Contrast : {contrast:.1f}, Brightness : {brightness}", datetime.now()))
        
    
    #원래 num키로 1이 녹화시작, 2가 종료였지만 스페이스바로 급하게 바꾸다보니 코드가 조금 지저분한듯.. 추후 수정해야겟음
    if key == ord(' ') and not recording:
        print("Recording Start")
        start_time = datetime.now()
        recording = True
        filename = os.path.join(path, f"{get_timestamp()}.avi")    
        # capture.get(3) : 영상 가로 해상도, capture.get(4) : 영상 세로 해상도, 현재의 카메라 해상도를 그대로 가져온다는 의미임
        out = cv.VideoWriter(filename, fourcc, 30.0, (int(capture.get(3)), int(capture.get(4))))
    
    elif key == ord(' ') and recording:
        print('Recording Stop')
        recording = False
        out.release()
        text_queue.append((f"{get_timestamp()}.avi - Video Saved", datetime.now()))

        
    elif key == ord('s'):
        filename = os.path.join(path, f"{get_timestamp()}.png")
        cv.imwrite(filename, frame)
        text_queue.append((f"{get_timestamp()}.png - Screenshot Saved", datetime.now()))

    elif key == 27:
        break

    if recording and out is not None:
        out.write(frame)
    
capture.release()

if out:
    out.release()
    
cv.destroyAllWindows()
    
