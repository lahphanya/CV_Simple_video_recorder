# CV_Simple_video_recorder

해당 프로그램은 OpenCV를 이용한 간단한 Video Recorder로써 밑에 서술한 기능들을 모두 사용 가능함

기본적으로 display_frame 과 frame 으로 나눠서 표시하며, display_frame은 현재 사용자의 화면을 보여주고. frame 은 녹화된 순수한 형태로 저장됨

spacebar : 해당 비디오의 녹화 및 종료버튼 기능을 함, 이때 종료되는 즉시 자동으로 바탕화면에 time_stamp 형식으로 파일이 저장
  이때, 비디오 녹화의 경우 밑에 녹화 시간과 종료 후 time_stamp 형식으로 저장 후 display_frame 에 표시
  
S : 해당 비디오화면의 간단한 스크린샷 기능을 함 
  이때 저장후, 해당파일의 이름을 time_stamp 형식으로 저장 후 display_frame 에 표시
  
[ ] : 밝기를 올려주고 낮춰주는 기능으로, 녹화하는 도중 실시간으로 변경 가능

, . : 대비(contrast)를 올려주고 낮춰주는 기능으로 녹화하는 도중 실시간으로 변경 가능

R : 밝기(Brightness)와 대비(Contrast)를 초기화(밝기:0, 대비:1.0)시켜주는 기능

esc : 해당 recorder를 종료시켜주는 기능
